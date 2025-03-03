from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell


class Key(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(140, LIGHTRED)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("You got a Key!")
            return True

        return False
    

    
