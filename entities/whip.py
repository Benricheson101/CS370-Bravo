from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Whip(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(244, WHITE)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Im indiana jonesing it!!!!!")
            return True
        
        return False
    
    #TODO: get player count of whips
        #button to use whip
        #in use whip function, have whip spin around
        #if whip hits enemy, it dies
        #if whip hits wall, chance for wall to break
        