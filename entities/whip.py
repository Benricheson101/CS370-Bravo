from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Whip(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(244)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Im indiana jonesing it!!!!!")
            #from level.level_load import game_instance
            #if game_instance:
                #game_instance.whip_count += 1
            return True
        return False

    #TODO: get player count of whips
        #button to use whip
        #in use whip function, have whip spin around
        #if whip hits enemy, it dies
        #if whip hits wall, chance for wall to break

