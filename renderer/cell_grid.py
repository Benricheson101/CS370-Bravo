from typing import TYPE_CHECKING, Optional, List, Tuple, Union
from pygame import Rect, Surface, Vector2
import pygame
from pygame.color import Color
from pygame.sprite import Group
from constants import COLORS, GRID_CELL_HEIGHT, GRID_CELL_WIDTH, LIGHTGRAY, RED, TRANSPARENT, WHITE
from entities.border import Border
from entities.char import Char
from entities.cursor import Cursor, CursorType
from renderer.cell import Cell
from util.color import ColorValue, to_color
from util.math import clamped_add
from random import randint, random, choice

if TYPE_CHECKING:
    from game import Game

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
    group: Group
    surface: Surface
    rect: Rect
    game: "Game"

    fill: Color
    fg: Tuple[Color, Color]
    bg: Tuple[Color, Color]

    cur_pos: GridPosition # cursor position for functions like write and writeln. note that put() isn't related to this
    cur_type: int
    blink: bool
    blink_visible: bool
    # cur_pos_current: Optional[GridPosition]

    cursor: Cursor

    def __init__(
            self,
            game: "Game",
            grid_size: GridPosition,
            cell_size: GridPosition = (GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
            offset = (0, 0),
            fill = Color(0x00000000),
    ):
        """
        Creates a CellGrid

        Args:
            game: the Game this grid is associated with
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

        self.cur_pos = (0, 0)
        self.cur_type = 3
        self.blink_visible = False
        self.blink = False
        # self.cur_pos_current = None

        self.fg = (WHITE, LIGHTGRAY)
        self.bg = (TRANSPARENT, TRANSPARENT)
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.surface = Surface((cell_width * cols, cell_height * rows), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=offset)

        self.surface.fill(fill)
        self.group = Group()

        self.game = game

        self.flash_counter = 14
        self.cursor = Cursor(CursorType.SolidBlock, self.fg)

    def put(self, pos: GridPosition, sprite: Cell, _add_to_grid = True):
        col, row = pos

        assert col >= 0 and col < self.cols, "col position must be within grid bounds"
        assert row >= 0 and row < self.rows, "row position must be within grid bounds"

        sprite.grid = self
        sprite.x = col
        sprite.y = row


        cell_x = col * self.cell_width
        cell_y = row * self.cell_height

        sprite.rect.topleft = (int(cell_x), int(cell_y))

        # if self.at(pos) is not None:
        #     self.remove(pos)

        if _add_to_grid:
            self.grid[row][col] = sprite

        self.group.add(sprite)
        sprite.visible = True


    def remove(self, pos: GridPosition) -> Optional[Cell]:
        col, row = pos

        cel = self.grid[row][col]
        if cel is None:
            return None

        self.grid[row][col] = None
        self.group.remove(cel)
        cel.grid = None
        cel.visible = False

        return cel

    def at(self, pos: GridPosition) -> Optional[Cell]:
        return self.grid[pos[1]][pos[0]]

    def move_to(self, pos: GridPosition, sprite: Cell) -> Optional[Cell]:
        """Moves a sprite on the grid by **replacing anything in its new position**"""
        col, row = pos

        assert col >= 0 and col < self.cols, f"col position must be within grid bounds (got {col})"
        assert row >= 0 and row < self.rows, f"row position must be within grid bounds (got {row})"

        pos_before = sprite.pos

        at = self.at(pos)
        if at and not at.on_collision(sprite):
            return None

        assert sprite.pos == pos_before, \
            f"cell position changed in on_collision (before {pos_before}, after {sprite.pos}). if this is intentional, be sure to return `False` from `on_collision`"

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
        self.surface.fill(self.fill)
        for sprite in self.group:
            self.surface.blit(sprite.image, sprite.rect)
        parent.blit(self.surface, self.rect)

    def update(self):
        if self.cur_type != CursorType.Invisible.value:
            # HACK: superimpose the cursor instead of replacing a grid space with it
            if self.cursor.visible:
                self.group.remove(self.cursor)
                self.cursor.visible = False

            self.put(self.cur_pos, self.cursor, _add_to_grid=False)
        else:
            if self.cursor.visible:
                self.group.remove(self.cursor)
                self.cursor.visible = False

        self.group.update(new_fg=COLORS[self.flash_counter])

    def _flip_blink(self):
        self.blink_visible = not self.blink_visible

    def _flip_flash(self):
        self.flash_counter += 1
        if self.flash_counter > 15:
            self.flash_counter = 13

    def get_random_empty_tiles(grid) -> List[Tuple[int, int]]:
        """
        Returns a list of (x, y) coordinates for every empty tile in the grid.

        Args:
            grid: The CellGrid object.

        Returns:
            A list of (x, y) coordinate tuples.
        """

        empty_tiles = []
        for row in range(grid.rows):
            for col in range(grid.cols):
                if grid.at((col, row)) is None:  # Check if the cell is empty
                    empty_tiles.append((col, row))


        if empty_tiles:  # Check if any empty tiles were found
            return choice(empty_tiles)

    # emulating DOS screen functions

    def cur(self, c: int):
        """
        sets the type of the cursor

        Args:
            c: (int 1-3) the cursor type
                1: underline
                2: solid block
                3: invisible
        """
        self.cur_type = c

    def bak(self, c: Union[Color, int], m: Union[Color, int]):
        """
        Sets the background color of text

        Args:
            c: the color when in color mode
            m: the color when in monochrome mode
        """
        self.bg = (
            c if isinstance(c, Color) else COLORS[c],
            m if isinstance(m, Color) else COLORS[m],
        )

    def col(self, c: ColorValue, m: ColorValue):
        """
        Sets the color for text written using the dos-like methods

        Args:
            c: the color when in color mode
            m: the color when in monochrome mode
        """
        c1, blink = to_color(c)
        m1, _ = to_color(m)
        self.fg = (c1, m1)
        self.blink = blink

        # self.color = (
        #     c if isinstance(c, Color) else COLORS[c],
        #     m if isinstance(m, Color) else COLORS[m],
        # )

    def clrscr(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.remove((col, row))

    def delline(self):
        """
        Deletes the line the cursor is on and shifts all of the lines below it up by one. The cursor does not move
        """
        for x in range(self.cols):
            self.remove((x, self.cur_pos[1]))

        for col in range(0, self.cols):
            for row in range(self.cur_pos[1], self.rows):
                if (sprite := self.at((col, row))) is not None:
                    self.move_to((col, row - 1), sprite)

    def insline(self):
        """
        Inserts a new line at the cursor and shifts all of the lines below it down by one. The last line is removed. The cursor does not move
        """

        for x in range(self.cols):
            self.remove((x, self.rows - 1))

        for col in range(0, self.cols):
            for row in range(self.cur_pos[1], self.rows - 1):
                if (sprite := self.at((col, row))) is not None:
                    self.move_to((col, row + 1), sprite)

    def gotoxy(self, x: int, y: int):
        """
        "GotoXY positions the cursor at (X,Y), X in horizontal, Y in vertical direction relative to the origin of the current window. The origin is located at (1,1), the upper-left corner of the window"
            - from: https://www.freepascal.org/docs-html/rtl/crt/gotoxy.html
        """
        self.cur_pos = (x - 1, y - 1)

    def writeln(self, msg: str = ''):
        if msg is not None:
            self.write(msg)
        self.cur_pos = (0, self.cur_pos[1] + 1)

    def write(self, msg: str, flash: bool = False):
        start = self.cur_pos[0]
        end = self.cur_pos[0] + len(msg)

        assert end < self.cols, f"message extends off the edge of the screen, start: {self.cur_pos}, end: {(end, self.cur_pos[1])}"

        # for i in range(start, end):
        # TODO: put these in a sprite group
        for i, char in enumerate(msg):
            self.remove((start + i, self.cur_pos[1]))
            self.put(
                (start + i, self.cur_pos[1]),
                Char(
                    char,
                    fg=self.fg[0],
                    bg=self.bg[0],
                    flash=flash,
                    blink=self.blink
                )
            ) # TODO: monochrome mode

        self.cur_pos = (end, self.cur_pos[1])

    def flash(self, xpos: int, ypos: int, msg: str):
        oldcur = self.cur_pos
        self.gotoxy(xpos, ypos)
        self.write(msg, flash=True)
        self.cur_pos = oldcur

    def border(self):
        bc = randint(0, 7) + 8
        bb = randint(0, 6) + 1

        for i in range(0, self.cols):
            self.put((i, self.rows - 1), Border(bc, bb))
            self.put((i, 0), Border(bc, bb))

        for i in range(self.rows):
            self.put((self.cols - 1, i), Border(bc, bb))
            self.put((0, i), Border(bc, bb))
