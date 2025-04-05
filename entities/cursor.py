from typing import Tuple
from pygame import Color
from renderer.cell import Cell
from enum import Enum

from util.color import ColorValue


class CursorType(Enum):
    Underline = 1
    SolidBlock = 2
    Invisible = 3

    def to_char(self) -> int:
        match self.value:
            case 1: return 95
            case 2: return 219
            case 3: return 0

class Cursor(Cell):
    type: CursorType

    def __init__(self, cur_type: CursorType, fg: Tuple[ColorValue, ColorValue]) -> None:
        super().__init__()
        self.type = cur_type
        self.col(*fg)
        self.load_dos_char(cur_type.to_char())
        self.blink = True

    def update(self, **kwargs):
        self.load_dos_char(self.type.to_char())
        return super().update(**kwargs)

    def on_collision(self, cell: "Cell") -> bool:
        return True
