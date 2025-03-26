from typing import Optional
from pygame import Color
from constants import TRANSPARENT, WHITE
from renderer.cell import Cell


class Char(Cell):
    def __init__(
        self,
        char: str,
        fg: Color = WHITE,
        bg: Color = TRANSPARENT,
        flash: bool = False,
        blink: bool = False,
    ) -> None:
        super().__init__()

        assert len(char) == 1, f"Char cell can only hold one character (got: {char})"

        # self.bg = bg
        # self.fg = fg

        # FIXME: add mono colors here
        self.col(fg, TRANSPARENT)
        self.bak(bg, TRANSPARENT)
        self.char = ord(char)
        self.flash = flash
        self.blink = blink

        self.image.fill(bg)
        self.load_dos_char(self.char, fg)

    def update(self, new_fg: Optional[Color] = None, **kwargs) -> None:
        if self.flash and new_fg:
            # self.fg = (new_fg, self.fg[1])
            self.col(new_fg, self.fg[1])
            self.load_dos_char(self.char, None) # FIXME

    def on_collision(self, cell: "Cell") -> bool:
        return False
