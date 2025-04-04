from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Invisible(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(2, 7)
        self.load_dos_char(173)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('Oh no, a temporary Blindness Potion!')
            cell.make_invisible(3000)
        
            return True
        return False

