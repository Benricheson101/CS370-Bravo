from pygame import Color
from renderer.cell import Cell
from enum import Enum


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
    def __init__(self, cur_type: CursorType, fg: Color) -> None:
        super().__init__()
        self.load_dos_char(cur_type.to_char(), fg)
        self.blink = True

    def on_collision(self, cell: "Cell") -> bool:
        return True
