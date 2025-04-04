from entities.player import Player
from renderer.cell import Cell

class River(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.bak(1, 7)
        self.col(9, 0)
        self.load_dos_char(247)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            print('You cannot travel through Water.')
        return False


