from constants import PURPLE
from entities.player import Player
from renderer.cell import Cell

class Teleport(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(PURPLE)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Teleport scroll!")
            return True

        return False