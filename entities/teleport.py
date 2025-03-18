from constants import LIGHTMAGENTA
from entities.player import Player
from renderer.cell import Cell


class Teleport(Cell):
    def __init__(self) -> None:
        super().__init__()
        # self.load_sprite("./sprites/teleport.png")
        self.load_dos_char(24, LIGHTMAGENTA)

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        if isinstance(cell, Player):
            print("Player hit a Teleport scroll!")
            
            empty_cell = cell.grid.get_random_empty_tiles()
            
            cell.move_to((empty_cell))
            self.grid.remove((self.x, self.y))
                

            return False

        return False
    
    #TODO Make the object be collectable and then press the T key to run the teleport shit