import pygame
from constants import BLACK, WHITE, YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid

class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        # Player color and sprite
        self.col(14, WHITE)
        self.load_dos_char(2)
        self.last_move_time = 0 # Track movement delay (milliseconds)
        #         WHIP
        self.whip_animation_frames = 0
        self.whip_animation_active = False
        self.whip_direction = 0
        self.whip_symbols = ['\\', 'ƒ', '/', '≥', '\\', 'ƒ', '/', '≥']
        
        
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


    def update(self, **kwargs) -> None:
        assert self.grid

        current_time = pygame.time.get_ticks()

        # restore visibility if time is up
        if self.is_invisible:
            # print(f"[DEBUG] invisibility ends in {self.invisible_until - current_time}ms")
            if current_time >= self.invisible_until:
                # print("[DEBUG] Restoring sprite now!")
                self.load_dos_char(2)
                self.is_invisible = False

        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_j]:
                    dx = -1
                elif event.key in [pygame.K_RIGHT, pygame.K_l]:
                    dx = 1
                elif event.key in [pygame.K_UP, pygame.K_i]:
                    dy = -1
                elif event.key in [pygame.K_DOWN, pygame.K_m]:
                    dy = 1

        # Arrow keys override IJKM
        if keys[pygame.K_LEFT] ^ keys[pygame.K_RIGHT]:
            dx = 1 if keys[pygame.K_RIGHT] else -1
        if keys[pygame.K_UP] ^ keys[pygame.K_DOWN]:
            dy = 1 if keys[pygame.K_DOWN] else -1

        # IJKM and diagonals
        if dx == 0 and dy == 0:
            if keys[pygame.K_j]: dx = -1
            if keys[pygame.K_l]: dx = 1
            if keys[pygame.K_i]: dy = -1
            if keys[pygame.K_m]: dy = 1
            if keys[pygame.K_u]: dx, dy = -1, -1
            elif keys[pygame.K_o]: dx, dy = 1, -1
            elif keys[pygame.K_n]: dx, dy = -1, 1
            elif keys[pygame.K_COMMA]: dx, dy = 1, 1

        # Numpad movement
        if keys[pygame.K_KP4]: dx = -1
        elif keys[pygame.K_KP6]: dx = 1
        if keys[pygame.K_KP8]: dy = -1
        elif keys[pygame.K_KP2]: dy = 1
        if keys[pygame.K_KP7]: dx, dy = -1, -1
        elif keys[pygame.K_KP9]: dx, dy = 1, -1
        elif keys[pygame.K_KP1]: dx, dy = -1, 1
        elif keys[pygame.K_KP3]: dx, dy = 1, 1

        # Move if input is valid and enough time passed
        if (dx != 0 or dy != 0) and (current_time - self.last_move_time > 100):
            self.grid.move(pygame.Vector2(dx, dy), self)
            self.last_move_time = current_time
        
                # Handle whip animation
        if self.whip_animation_active:
            self.update_whip_animation()
        
        # Check for whip usage
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not self.whip_animation_active:
            self.use_whip()

        super().update()
            

    def on_collision(self, cell: "Cell") -> bool:
        return False

    def get_player_position(self) -> tuple[int, int]:
        """
        Gets the player's current position on the grid.
        """
        print(self.x, self.y)
        return self.x, self.y
