from constants import LIGHTCYAN
from entities.player import Player
from renderer.cell import Cell


class Gem(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(4, LIGHTCYAN)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Gem!")
            from level.level_load import game_instance
            if game_instance:  
                game_instance.gem_count += 1
            return True
        
        return False
