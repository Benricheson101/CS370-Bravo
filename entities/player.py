import pygame
from constants import YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid


class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(2, YELLOW)
        self.last_move_time = 0 # Track movement delay (milliseconds)

    def update(self, **kwargs) -> None:
        assert self.grid
        
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0  # Movement direction

        # Handle movement input (one direction per axis)
        if keys[pygame.K_LEFT] ^ keys[pygame.K_RIGHT]:
            dx = 1 if keys[pygame.K_RIGHT] else -1
            
        if keys[pygame.K_UP] ^ keys[pygame.K_DOWN]:
            dy = 1 if keys[pygame.K_DOWN] else -1

        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time > 150:  # 150ms delay for tile movement
            self.grid.move(pygame.Vector2(dx, dy), self)  # Use the grid's move function
            self.last_move_time = current_time  # Update movement timer



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
 
