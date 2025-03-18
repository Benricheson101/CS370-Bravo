'''import pygame
from constants import YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid


class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(2, YELLOW)

    def update(self) -> None:
        assert self.grid

        keys = pygame.key.get_pressed()
        d = pygame.math.Vector2()

        if keys[pygame.K_LEFT] ^ keys[pygame.K_RIGHT]:
            d.x = 1 if keys[pygame.K_RIGHT] else -1

        if keys[pygame.K_UP] ^ keys[pygame.K_DOWN]:
            d.y = 1 if keys[pygame.K_DOWN] else -1

        if d.length() > 0:
            d.normalize_ip()
            # FIXME: add a movement delay
            self.move(d) # moves player in direction
            # TODO: sound here



    def on_collision(self, cell: "Cell") -> bool:

        return False
    def get_player_position(self) -> tuple[int, int]:
        """
        Gets the player's current position on the grid.

        Returns:
            A tuple of (x, y) coordinates representing the player's position.
        """
        print(self.x, self.y)
        return self.x, self.y'''

import pygame
from time import time
from constants import YELLOW
from renderer.cell import Cell
from renderer.cell_grid import CellGrid

class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(2, YELLOW)

        self.last_move_time = time()  # Time of last movement
        self.move_delay = 0.1  # 100ms delay between moves (adjustable)

    def update(self, **kwargs) -> None:
        assert self.grid

        current_time = time()
        if current_time - self.last_move_time < self.move_delay:
            return  # Prevent movement if delay hasn't passed

        keys = pygame.key.get_pressed()
        d = pygame.math.Vector2(0, 0)  # Start with no movement

        # Horizontal movement (left and right)
        if keys[pygame.K_LEFT]:
            d.x = -1
        elif keys[pygame.K_RIGHT]:
            d.x = 1

        # Vertical movement (up and down)
        if keys[pygame.K_UP]:
            d.y = -1
        elif keys[pygame.K_DOWN]:
            d.y = 1

        if d.length() > 0:
            # Normalize the vector (automatically handles diagonal normalization)
            d = d.normalize()

            # Move the player in the direction of the vector
            self.move(d)
            self.last_move_time = current_time

            # Optional: Add sound here if needed (example)
            # move_sound.play()

    def on_collision(self, cell: "Cell") -> bool:
        # Implement collision logic here if needed
        return False

    def get_player_position(self) -> tuple[int, int]:
        """
        Gets the player's current position on the grid.

        Returns:
            A tuple of (x, y) coordinates representing the player's position.
        """
        return self.x, self.y
