from entities.player import Player
from renderer.cell import Cell


class Gem(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_sprite("./sprites/gem.png")

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Gem!")
            return True

        return False
