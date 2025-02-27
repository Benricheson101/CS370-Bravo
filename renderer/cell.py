from abc import abstractmethod
from typing import Optional, TYPE_CHECKING
from pygame import Rect, Surface, Vector2
import pygame
from pygame.color import Color
from pygame.sprite import Sprite
from constants import BLACK, GRID_CELL_HEIGHT, GRID_CELL_WIDTH
from assets.spritesheet import dos_sprites

if TYPE_CHECKING:
    from renderer.cell_grid import CellGrid, GridPosition


class Cell(Sprite):
    rect: Rect
    image: Surface
    x: int
    y: int

    def __init__(self, width = GRID_CELL_WIDTH, height = GRID_CELL_HEIGHT) -> None:
        super().__init__()

        self.image = Surface((width, height), pygame.SRCALPHA)
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

    @abstractmethod
    def on_collision(self, cell: "Cell") -> bool:
        """
        A function that runs when another cell collides with the current cell.

        Return: True to replace `cell` else `False` to prevent movement
        """
        return True

    def load_sprite(self, path: str):
        img = pygame.image.load(path).convert_alpha()

        scale_factor = self.rect.size[0] / img.get_size()[0]
        scaled_img = pygame.transform.scale_by(img, scale_factor)

        print(self.__class__.__name__, scale_factor)

        rect = scaled_img.get_rect(
            center=self.rect.center
        )

        self.image.blit(scaled_img, rect)

    def load_dos_char(self, n: int, color: Color = BLACK):
        img = dos_sprites().sprite((n, 0))

        color_img = Surface(self.image.get_size(), pygame.SRCALPHA)
        color_img.fill(color)

        img.blit(color_img, (0, 0), special_flags=pygame.BLEND_MAX)

        scale_factor = self.rect.size[0] / img.get_size()[0]
        scaled_img = pygame.transform.scale_by(img, scale_factor)

        rect = scaled_img.get_rect(
            center=self.rect.center
        )

        self.image.blit(scaled_img, rect)
