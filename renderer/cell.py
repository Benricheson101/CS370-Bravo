from abc import abstractmethod
from typing import Optional, TYPE_CHECKING, Tuple
from pygame import Rect, Surface, Vector2
import pygame
from pygame.color import Color
from pygame.sprite import WeakSprite
from constants import GRID_CELL_HEIGHT, GRID_CELL_WIDTH, TRANSPARENT
from renderer.spritesheet import dos_sprites
from util import ColorValue, to_color

if TYPE_CHECKING:
    from renderer.cell_grid import CellGrid, GridPosition


class Cell(WeakSprite):
    rect: Rect
    image: Surface
    x: int
    y: int
    blink: bool
    fill_color: Color

    fg: Tuple[Color, Color]
    bg: Tuple[Color, Color]

    def __init__(self, width = GRID_CELL_WIDTH, height = GRID_CELL_HEIGHT) -> None:
        super().__init__()

        self.height = height
        self.width = width

        self.rect = Rect(0, 0, width, height)

        self.image = Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.grid: Optional["CellGrid"] = None
        self.walkable = True
        self.blink = False

        self.bg = (TRANSPARENT, TRANSPARENT)
        self.fg = (TRANSPARENT, TRANSPARENT)

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

    def load_dos_char(self, n: int, color: Optional[Color] = None):
        if color is not None:
            print(f"WARNING: self.image.fill is deprecated in favor of self.col() in entity classes (in {self.__class__.__name__})")

        img = dos_sprites().sprite((n, 0))

        color_img = Surface(self.image.get_size(), pygame.SRCALPHA)
        color_img.fill(color or self.fg[0])

        img.blit(color_img, (0, 0), special_flags=pygame.BLEND_MAX)

        scale_factor = self.rect.size[0] / img.get_size()[0]
        scaled_img = pygame.transform.scale_by(img, scale_factor)

        self.sprite = scaled_img
        self.image.blit(self.sprite, self.rect)

    @property
    def pos(self) -> "GridPosition":
        return self.x, self.y

    def _blink(self):
        assert self.grid

        if self.grid.blink_visible:
            self.image = self.sprite.copy()
        else:
            self.image.fill(self.bg[0])

    def update(self, **kwargs):
        """
        Called on every frame.

        **IMPORTANT** if you are using blinking text AND overriding update(), make sure you call `super().update()` or `self._blink()` in your update() function
        """
        if self.blink and self.grid is not None:
            self._blink()

    def col(self, c: ColorValue, m: ColorValue, blink: Optional[bool] = None):
        """
        Sets the foreground color of the cell

        Args:
            c: the color when in color mode
            m: the color when in monochrome mode
            blink: if the loaded sprite should blink
        """
        c1, blink1 = to_color(c, blink)
        m1, _ = to_color(m)

        self.fg = (c1, m1)
        self.blink = blink1

    def bak(self, c: ColorValue, m: ColorValue):
        """
        Sets the background fill color of the cell

        Args:
            c: the color when in color mode
            m: the color when in monochrome mode
        """
        c1, _ = to_color(c)
        m1, _ = to_color(m)
        self.bg = (c1, m1)
