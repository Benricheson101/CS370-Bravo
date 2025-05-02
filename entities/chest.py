"""import random
from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Chest(Cell):
    def __init__(self, color: Color) -> None:
        super().__init__()
        self.bak(4)
        self.col(14)
        self.load_dos_char(67)
           

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('You stumbled across a Chest.')
            from level.level_load import game_instance
            if game_instance:
                
                game_instance.player.whips = random.randint(2,4)
                game_instance.player.gems = random.randint(2, game_instance.difficulty + 1)
                
                return True
        return False
    
    def update(self, **kwargs):
        return super().update(**kwargs)"""