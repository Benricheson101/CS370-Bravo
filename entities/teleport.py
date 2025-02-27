from constants import PINK
from entities.player import Player
from renderer.cell import Cell

class Teleport(Cell):
    def __init__(self) -> None:
        super().__init__()
        # self.load_sprite("./sprites/teleport.png")
        self.load_dos_char(24, PINK)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Teleport scroll!")
            return True

        return False
