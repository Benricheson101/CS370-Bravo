from typing import Optional
from pygame import Color
from constants import GREEN, RED, TRANSPARENT, WHITE
from renderer.cell import Cell


class Char(Cell):
    def __init__(self, char: str, fg: Color = WHITE, bg: Color = TRANSPARENT, flash: bool = False) -> None:
        super().__init__()

        assert len(char) == 1, f"Char cell can only hold one character (got: {char})"

        self.bg = bg
        self.fg = fg
        self.char = ord(char)
        self.flash = flash

        self.image.fill(bg)
        self.load_dos_char(self.char, fg)

    def update(self, new_fg: Optional[Color] = None) -> None:
        if self.flash and new_fg is not None:
            self.fg = new_fg

            self.load_dos_char(self.char, self.fg)

    def on_collision(self, cell: "Cell") -> bool:
        return False
