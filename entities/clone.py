from pygame import Surface, Color
from constants import LIGHTGREEN
from entities.player import Player
from renderer.cell import Cell

class Clone(Player):
    def __init__(self) -> None:
        super().__init__()

        self.clone = True

        # Redefine the appearance
        self.fg = (Color(0, 255, 0), Color(0, 255, 0))  # green in color & monochrome
        self.bg = (Color(0, 0, 0, 0), Color(0, 0, 0, 0))  # transparent background

        # Recreate the visual appearance
        self.load_dos_char(2)  # Re-load the same DOS char but with new fg/bg

    def use_whip(self) -> None:
        """Prevent clone from whipping."""
        pass

    def on_collision(self, cell: "Cell") -> bool:
        from entities.enemy import Enemy
        from entities.lava import Lava

        if isinstance(cell, (Enemy, Lava)):
            if self.grid:
                print("Clone removed!")
                self.grid.remove((self.x, self.y))
            return True

        return super().on_collision(cell)
