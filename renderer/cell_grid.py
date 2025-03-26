from typing import TYPE_CHECKING, Optional, List, Tuple, Union
from pygame import Rect, Surface, Vector2
import pygame
from pygame.color import Color
from pygame.sprite import Group
from constants import COLORS, GRID_CELL_HEIGHT, GRID_CELL_WIDTH, LIGHTGRAY, RED, TRANSPARENT, WHITE
from entities.char import Char
from entities.cursor import Cursor, CursorType
from renderer.cell import Cell
from util import ColorValue, clamped_add, to_color
import random

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
    cur_pos_current: Optional[GridPosition]

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
        self.cur_pos_current = None

        self.fg = (WHITE, LIGHTGRAY)
        self.bg = (TRANSPARENT, TRANSPARENT)
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.surface = Surface((cell_width * cols, cell_height * rows), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=offset)

        self.surface.fill(fill)
        self.group = Group()

        self.game = game

        self.flash_counter = 14

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
        # self.group.update()
        self.surface.fill(self.fill)
        self.group.draw(self.surface)
        parent.blit(self.surface, self.rect)

    def update(self):
        new_fg = None

        if pygame.time.get_ticks() % 2 == 0:
                new_fg = COLORS[self.flash_counter]

                self.flash_counter += 1
                if self.flash_counter > 15:
                    self.flash_counter = 13

        # if self.blink_visible and not isinstance(self.at(self.cur_pos), Cursor):
        if self.cur_type != CursorType.Invisible.value:
            self.put(self.cur_pos, Cursor(CursorType(self.cur_type), fg=RED))
            self.cur_pos_current = self.cur_pos
        else:
            if self.cur_pos_current:
                self.remove(self.cur_pos_current)
                self.cur_pos_current = None
        # elif not self.blink_visible and isinstance(self.at(self.cur_pos), Cursor):
        #     assert self.cur_pos_current
        #     self.remove(self.cur_pos_current)
        #     self.cur_pos_current = None


        self.group.update(new_fg=new_fg)

        # counter = 14
        # procedure Flash(XPos,YPos:byte;Message:Str80);
        #  var Counter : integer;
        #  begin
        #   Counter := 14;
        #   ClearKeys;
        #   repeat
        #    Counter := Counter + 1;
        #    if Counter > 15 then Counter := 13;
        #    col(Counter,15);
        #    delay(20);
        #    print(XPos,YPos,Message);
        #   until keypressed;
        #   Restore_Border;
        #  end;

    def _flip_blink(self):
        self.blink_visible = not self.blink_visible

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
            return random.choice(empty_tiles)

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

        # match c:
        #     case 1:
        #         print("1!")
        #
        #     case 2:
        #         print("2")
        #
        #     case 3:
        #         print("")

# procedure Cur(Num:byte);
#  var Result : Registers;
#  begin
#   Result.AX := $100;
#   with Result do
#    if Color then
#     case Num of
#      1:CX:=$707;   { Underline   }
#      2:CX:=$8;     { Solid Block }
#      3:CX:=$2000;  { Invisible   }
#     end
#    else
#     case Num of
#      1:CX:=$C0D;
#      2:CX:=$E;
#      3:CX:=$2000;
#     end;
#    intr($10,Result);
#  end; { Cur }

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

        # group = Group()
        #
        # sprites = [Char(c, fg=self.color[0]) for c in msg]
        # group.add(sprites)
        #
        # for i, s in enumerate(sprites):
        #     self.put((xpos - 1 + i, ypos - 1), s)
        #
        # self.flash_groups.append(group)
