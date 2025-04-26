from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Tunnel(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(239)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('You passed through a secret Tunnel!')
        
            return True
        return False

