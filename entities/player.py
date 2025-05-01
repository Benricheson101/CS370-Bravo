import pygame
import threading
from constants import BLACK, WHITE, YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from Sound import SoundEffects
from random import random
from entities.char import Char
from pygame.color import Color
from random import randint
from util.state import State, StateMachine

from util.math import clamped_add


class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        # Player color and sprite
        self.col(14, WHITE)
        self.load_dos_char(2)
        self.last_move_time = 0  # Track movement delay (milliseconds)

        # WHIP
        self.whip_animation_frames = 0
        self.whip_animation_active = False
        self.whip_direction = 0

        # Teleport
        self.collected_teleports = 0

    # Dead
        self.is_dead = False

    # For invisible.py
        self.invisible_until = 0  # Time (ms) when invisibility ends
        self.is_invisible = False


    def make_invisible(self, duration: int):
        """
        Temporarily turns the player invisible by replacing the sprite with a blank character.
        """
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Reset image
        self.load_dos_char(0)  # blank/invisible
        self.invisible_until = pygame.time.get_ticks() + duration
        self.is_invisible = True

    def dead(self):
        from level.level_load import game_instance
        sm = game_instance.sm
        grid = sm.current_state.grid
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        bb = randint(0, 7) + 8
        grid.gotoxy(self.x + 1, self.y + 1)
        grid.write('*', True)
        grid.col(16, 16)
        grid.col(bb, 7)
        grid.print(27, 1, 'YOU HAVE DIED!!')
        sm.current_state.pause(True)
        grid.flash(27, 25, 'Press any key to continue.')
        sm.current_state.pause_reason = "death"
        self.is_dead = True


    def update(self, **kwargs) -> None:
        if self.grid is None:
            print("self.grid is None for some reason")
            return

        current_time = pygame.time.get_ticks()

        # restore visibility if time is up
        if self.is_invisible:
            # print(f"[DEBUG] invisibility ends in {self.invisible_until - current_time}ms")
            if current_time >= self.invisible_until:
                # print("[DEBUG] Restoring sprite now!")
                self.load_dos_char(2)
                self.is_invisible = False

        self.sound_effects = SoundEffects()

        dx, dy = 0, 0
        moved = False  # Initialize moved variable here
        keys = pygame.key.get_pressed()

        # Note: You should handle events in the main game loop, not here
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key in [pygame.K_LEFT, pygame.K_j]:
        #             dx = -1
        #         elif event.key in [pygame.K_RIGHT, pygame.K_l]:
        #             dx = 1
        #         elif event.key in [pygame.K_UP, pygame.K_i]:
        #             dy = -1
        #         elif event.key in [pygame.K_DOWN, pygame.K_m]:
        #             dy = 1
        # Arrow keys override IJKM

        # Handle movement input (one direction per axis) On the Arrow Keys
        if keys[pygame.K_LEFT] ^ keys[pygame.K_RIGHT]:
            dx = 1 if keys[pygame.K_RIGHT] else -1
        if keys[pygame.K_UP] ^ keys[pygame.K_DOWN]:
            dy = 1 if keys[pygame.K_DOWN] else -1

        if dx == 0 and dy == 0:
            # Handle movement input for ASCII keys (IJKM)
            if keys[pygame.K_j]:  # Left
                dx = -1
            if keys[pygame.K_l]:  # Right
                dx = 1
            if keys[pygame.K_i]:  # Up
                dy = -1
            if keys[pygame.K_m]:  # Down
                dy = 1

            if keys[pygame.K_u]:  # Up-left
                dx, dy = -1, -1
            elif keys[pygame.K_o]:  # Up-right
                dx, dy = 1, -1
            elif keys[pygame.K_n]:  # Down-left
                dx, dy = -1, 1
            elif keys[pygame.K_COMMA]:  # Down-right
                dx, dy = 1, 1

        # Movement with numpad
        if keys[pygame.K_KP4]:  # Numpad 4 (Left)
            dx = -1
        elif keys[pygame.K_KP6]:  # Numpad 6 (Right)
            dx = 1
        if keys[pygame.K_KP8]:  # Numpad 8 (Up)
            dy = -1
        elif keys[pygame.K_KP2]:  # Numpad 2 (Down)
            dy = 1

        # Diagonal movement with numpad
        if keys[pygame.K_KP7]:  # Up-Left
            dx, dy = -1, -1
        elif keys[pygame.K_KP9]:  # Up-Right
            dx, dy = 1, -1
        elif keys[pygame.K_KP1]:  # Down-Left
            dx, dy = -1, 1
        elif keys[pygame.K_KP3]:  # Down-Right
            dx, dy = 1, 1

        if (dx != 0 or dy != 0) and (current_time - self.last_move_time > 100):
            # Play footstep sound in a separate thread
            self.play_sound_in_thread(self.sound_effects.FootStep)
            moved = self.grid.move(pygame.Vector2(dx, dy), self)
            self.last_move_time = current_time
            if not moved:
                # Play block sound in a separate thread
                self.play_sound_in_thread(self.sound_effects.BlockSound)

        # Handle whip animation
        if self.whip_animation_active:
            self.update_whip_animation()

        if keys[pygame.K_w] and not self.whip_animation_active:
            self.use_whip()
            # Play whip sound (using grab sound as a substitute)
            self.play_sound_in_thread(self.sound_effects.GrabSound)

         # Use teleport on 'T'
        from level.level_load import game_instance
        if keys[pygame.K_t] and game_instance.teleport_count > 0 and (current_time - self.last_move_time > 100):
            empty_cell = self.grid.get_random_empty_tiles()
            self.move_to(empty_cell)
            game_instance.teleport_count -= 1
            self.last_move_time = current_time
            print("Teleported using a scroll!")
            return  # Skip movement on teleport

        super().update()

    def play_sound_in_thread(self, sound_method, FastPC=True):
        """Run sound methods in a separate thread to avoid freezing the game"""
        sound_thread = threading.Thread(target=sound_method, args=(FastPC,))
        sound_thread.daemon = True  # Thread will close when program exits
        sound_thread.start()

    def update_whip_animation(self):
        current_time = pygame.time.get_ticks()
        if self.whip_animation_frames < len(self.whip_sequence):
            if current_time - self.last_whip_flash_time > 30:  # Delay between steps
                dx, dy, symbol = self.whip_sequence[self.whip_animation_frames]
                self.process_whip_hit(self.x + dx, self.y + dy, symbol)
                self.whip_animation_frames += 1
                self.last_whip_flash_time = current_time
        else:
            self.whip_animation_active = False
            self.whip_animation_frames = 0


    def use_whip(self):
        from level.level_load import game_instance
        if game_instance.whip_count < 1:
            self.play_sound_in_thread(self.sound_effects.BlockSound)
            return

        game_instance.whip_count -= 1
        self.whip_animation_active = True
        self.whip_animation_frames = 0
        self.whip_sequence = [
            (-1, -1, '\\'),
            ( 0, -1, '|'),
            ( 1, -1, '/'),
            ( 1,  0, '-'),
            ( 1,  1, '\\'),
            ( 0,  1, '|'),
            (-1,  1, '/'),
            (-1,  0, '-')
        ]
        self.last_whip_flash_time = pygame.time.get_ticks()


        self.play_sound_in_thread(self.sound_effects.GrabSound)

    def process_whip_hit(self, x: int, y: int, symbol: str):
        if not self.grid or x < 0 or y < 0 or x >= self.grid.cols or y >= self.grid.rows:
            return

        from level.level_load import game_instance
        power = getattr(game_instance, "whip_power", 2)


        from entities.whip import WhipFlash
        flash = WhipFlash(symbol, self.grid, (x, y))
        self.grid.fx_group.add(flash)

        cell = self.grid.at((x, y))
        if not cell:
            return


        if hasattr(cell, "is_enemy") and cell.is_enemy():
            self.grid.remove((x, y))
            game_instance.score += 10
            print(f"Enemy at ({x}, {y}) whipped!")

        elif hasattr(cell, "is_breakable_wall") and cell.is_breakable_wall():
            if random() < power / 7:
                self.grid.remove((x, y))
                print(f"Wall at ({x}, {y}) destroyed!")



    def on_collision(self, cell: "Cell") -> bool:
        self.play_sound_in_thread(self.sound_effects.BlockSound)
        assert self.grid and self.grid.game

        from entities.enemy import Enemy
        if isinstance(cell, Enemy):
            self.grid.game.gem_count -= 0 if self.grid.game.gem_count <= 0 else 1
            self.grid.remove(cell.pos)

            if self.grid.game.gem_count <= 0:
                self.dead()

        return False

    def get_player_position(self) -> tuple[int, int]:
        """
        Gets the player's current position on the grid.

        Returns:
            A tuple of (x, y) coordinates representing the player's position.
        """
        return self.x, self.y


