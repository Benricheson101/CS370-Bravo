from typing import Optional, TYPE_CHECKING
from pygame import Rect, Surface
from pygame.sprite import Sprite
from constants import GRID_CELL_HEIGHT, GRID_CELL_WIDTH

if TYPE_CHECKING:
    from renderer.cell_grid import CellGrid, GridPosition


class Cell(Sprite):
    rect: Rect
    image: Surface
    x: int
    y: int
    walkable: bool

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

    def move(self, pos: "GridPosition"):
        assert self.grid
        return self.grid.move(pos, self)

    def move_wrapping(self, move_delta: "GridPosition") -> Optional["Cell"]:
        assert self.grid
        return self.grid.move_wrapping(move_delta, self)
