from constants import LIGHTCYAN
from entities.player import Player
from renderer.cell import Cell


class Gem(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(4, LIGHTCYAN)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Gem!")
            return True

        return False
