from typing import Optional
from pygame import Surface, Vector2
from pygame.color import Color
from pygame.sprite import Group
from constants import GRID_CELL_HEIGHT, GRID_CELL_WIDTH
from renderer.cell import Cell
from util import clamped_add, wrapping_add


GridPosition = tuple[int, int]

class CellGrid:
    """
    Grid-based rendering. Given `rows` and `columns`, this class constructs a matrix of [Cell] objects and renders them to the screen

    **Important:** Grid coordinates are 0-indexed, and begin in the upper left corner.
    """

    rows: int
    cols: int
    cell_height: int
    cell_width: int
    grid: list[list[Optional[Cell]]]
    surface: Surface
    fill: Color

    def __init__(
            self,
            grid_size: GridPosition,
            cell_size: GridPosition = (GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
            offset = (0, 0),
            fill = Color(0x00000000),
    ):
        """
        Creates a CellGrid

        Args:
            grid_size: (cols, rows) in the grid
            cell_size: (width, height) of once cell
            offset: offset the position of the grid on the parent surface
            fill: the background fill color of the grid (empty spaces)
        """

        cols, rows = grid_size
        cell_width, cell_height = cell_size

        assert rows >= 0, "row count must be positive"
        assert cols >= 0, "col count must be positive"
        assert cell_height > 0, "cell height must be positive"
        assert cell_width > 0, "cell width must be positive"

        self.rows = rows
        self.cols = cols
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.fill = fill

        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.surface = Surface((cell_width * cols, cell_height * rows))
        self.rect = self.surface.get_rect(topleft=offset)

        self.surface.fill(fill)
        self.group = Group()

    def put(self, pos: GridPosition, sprite: Cell):
        col, row = pos

        assert col >= 0 and col < self.cols, "col position must be within grid bounds"
        assert row >= 0 and row < self.rows, "row position must be within grid bounds"

        sprite.grid = self
        sprite.x = col
        sprite.y = row


        cell_x = col * self.cell_width
        cell_y = row * self.cell_height

        sprite.rect.topleft = (int(cell_x), int(cell_y))

        self.grid[row][col] = sprite
        self.group.add(sprite)


    def remove(self, pos: GridPosition) -> Optional[Cell]:
        col, row = pos

        cel = self.grid[row][col]
        if cel is None:
            return None

        self.grid[row][col] = None
        self.group.remove(cel)
        cel.grid = None
        return cel

    def at(self, pos: GridPosition) -> Optional[Cell]:
        return self.grid[pos[1]][pos[0]]

    def move_to(self, pos: GridPosition, sprite: Cell) -> Optional[Cell]:
        """Moves a sprite on the grid by **replacing anything in its new position**"""
        col, row = pos

        assert col >= 0 and col < self.cols, f"col position must be within grid bounds (got {col})"
        assert row >= 0 and row < self.rows, f"row position must be within grid bounds (got {row})"

        at = self.at(pos)
        if at and not at.on_collision(sprite):
            return None

        removed = self.remove(pos)
        _sprite = self.remove((sprite.x, sprite.y))

        assert sprite == (_sprite or removed), f"somehow deleted a different sprite"

        self.put((col, row), sprite)

        return removed

    def move(self, move_delta: Vector2, sprite: Cell) -> Optional[Cell]:
        """Moves the given number of spaces but stops at the edges of the screen"""
        new_col = clamped_add(sprite.x, int(move_delta.x), self.cols-1)
        new_row = clamped_add(sprite.y, int(move_delta.y), self.rows-1)
        return self.move_to((new_col, new_row), sprite)

    def render(self, parent: Surface):
        self.group.update()
        self.surface.fill(self.fill)
        self.group.draw(self.surface)
        parent.blit(self.surface, self.rect)
