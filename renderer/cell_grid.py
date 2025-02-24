from typing import Optional
from pygame import Surface
from pygame.color import Color
from constants import GRID_CELL_HEIGHT, GRID_CELL_WIDTH
from renderer.cell import Cell


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

    def __init__(
            self,
            grid_size: tuple[int, int],
            cell_size: tuple[int, int] = (GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
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

        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.surface = Surface((cell_width * cols, cell_height * rows))
        self.rect = self.surface.get_rect(topleft=offset)

        self.surface.fill(fill)

    def put(self, pos: tuple[int, int], sprite: Cell):
        col, row = pos

        assert col >= 0 and col < self.cols, "col position must be within grid bounds"
        assert row >= 0 and row < self.rows, "row position must be within grid bounds"

        self.grid[row][col] = sprite

    def render(self, parent: Surface):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if not cell:
                    continue

                cell_x = x * self.cell_width
                cell_y = y * self.cell_height

                cell.rect.topleft = (int(cell_x), int(cell_y))

                cell.update(x=x, y=y)
                cell.render(self.surface)

        parent.blit(self.surface, self.rect)
