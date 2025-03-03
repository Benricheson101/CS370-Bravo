from constants import (
    LIGHTGRAY,
    BLACK
)
from entities.player import Player
from renderer.cell import Cell
# from level_load import load_level


class Stairs(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(LIGHTGRAY)
        self.load_dos_char(240, BLACK)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            # load_level(2)
            print("To the next level!")
            return True

        return False
