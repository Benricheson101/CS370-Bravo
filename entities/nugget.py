from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Nugget(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(12, 7)
        self.load_dos_char(15)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('You found a Gold Nugget...500 points!')
            return True
        return False


