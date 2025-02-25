from typing import Optional, TYPE_CHECKING
from pygame import Rect, Surface, Vector2
import pygame
from pygame.sprite import Sprite
from constants import GRID_CELL_HEIGHT, GRID_CELL_WIDTH

if TYPE_CHECKING:
    from renderer.cell_grid import CellGrid, GridPosition


class Cell(Sprite):
    rect: Rect
    image: Surface
    x: int
    y: int

    def __init__(self, width = GRID_CELL_WIDTH, height = GRID_CELL_HEIGHT) -> None:
        super().__init__()

        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.grid: Optional["CellGrid"] = None
        self.walkable = True

    def move_to(self, pos: "GridPosition"):
        assert self.grid
        return self.grid.move_to(pos, self)

    def move(self, pos: Vector2):
        assert self.grid
        return self.grid.move(pos, self)

    def on_collision(self, cell: "Cell") -> bool:
        """
        A function that runs when another cell collides with the current cell.

        Return: True to replace `cell` else `False` to prevent movement
        """
        return True

    def load_sprite(self, path: str):
        img = pygame.image.load(path)

        scale_factor = self.rect.size[0] / img.get_size()[0]
        scaled_img = pygame.transform.scale_by(img, scale_factor)

        rect = scaled_img.get_rect(
            center=self.rect.center
        )

        self.image.blit(scaled_img, rect)
