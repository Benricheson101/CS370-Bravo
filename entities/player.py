import pygame
import threading
from constants import BLACK, WHITE, YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from Sound import SoundEffects

class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        # FIXME: what is the monochrome color for here?
        self.col(14, WHITE)
        self.load_dos_char(2)
        self.last_move_time = 0 # Track movement delay (milliseconds)
        #         WHIP
        self.whip_animation_frames = 0
        self.whip_animation_active = False
        self.whip_direction = 0
        self.whip_symbols = ['\\', 'ƒ', '/', '≥', '\\', 'ƒ', '/', '≥']
        
        self.FastPC = True
        self.sound_effects = SoundEffects()

    def update(self, **kwargs) -> None:
        assert self.grid
        
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_j]:  # Left
                    dx = -1
                elif event.key in [pygame.K_RIGHT, pygame.K_l]:  # Right
                    dx = 1
                elif event.key in [pygame.K_UP, pygame.K_i]:  # Up
                    dy = -1
                elif event.key in [pygame.K_DOWN, pygame.K_m]:  # Down
                    dy = 1

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
            self.sound_effects.play_in_thread(self.sound_effects.FootStep, self.FastPC)
            moved = self.grid.move(pygame.Vector2(dx, dy), self)
            self.last_move_time = current_time
            if not moved:
                self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
        
            # Handle whip animation
        '''if self.whip_animation_active:
            self.update_whip_animation()'''

        ''' if keys[pygame.K_w] and not self.whip_animation_active:
            self.use_whip()
            # Play whip sound (using grab sound as a substitute)
            self.sound_effects.play_sound_in_thread(self.sound_effects.grab_sound)'''

        super().update()
            

    def play_sound_in_thread(self, sound_method, FastPC=True):
        """Run sound methods in a separate thread to avoid freezing the game"""
        sound_thread = threading.Thread(target=sound_method, args=(FastPC,))
        sound_thread.daemon = True  # Thread will close when program exits
        sound_thread.start()

    def on_collision(self, cell: "Cell") -> bool:
        self.sound_effects.play_sound_in_thread(self.sound_effects.BlockSound,True)
        
        return False

    def get_player_position(self) -> tuple[int, int]:
        """
        Gets the player's current position on the grid.

        Returns:
            A tuple of (x, y) coordinates representing the player's position.
        """
        print(self.x, self.y)
        return self.x, self.y
    
    ''' def use_whip(self):
        """
        Activate the whip animation and play whip sound
        """
        self.whip_animation_active = True
        self.whip_animation_frames = 0
        # Get direction from player's last movement or default to right
        # For now we'll just use a placeholder direction
        self.whip_direction = 0
    
    def update_whip_animation(self):
        """
        Update the whip animation frames
        """
        self.whip_animation_frames += 1
        # If animation is complete
        if self.whip_animation_frames >= len(self.whip_symbols):
            self.whip_animation_active = False
            self.whip_animation_frames = 0'''
