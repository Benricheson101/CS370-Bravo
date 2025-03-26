import pygame
from constants import BLACK, WHITE, YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid

class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        # FIXME: what is the monochrome color for here?
        self.col(14, WHITE)
        self.load_dos_char(2)
        self.last_move_time = 0 # Track movement delay (milliseconds)

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
            self.grid.move(pygame.Vector2(dx, dy), self)
            self.last_move_time = current_time
        '''if current_time - self.last_move_time > 150:  # 150ms delay for tile movement
            self.grid.move(pygame.Vector2(dx, dy), self)  # Use the grid's move function
            self.last_move_time = current_time  # Update movement timer'''

        super().update()

    def on_collision(self, cell: "Cell") -> bool:

        return False

    def get_player_position(self) -> tuple[int, int]:
        """
        Gets the player's current position on the grid.

        Returns:
            A tuple of (x, y) coordinates representing the player's position.
        """
        print(self.x, self.y)
        return self.x, self.y
