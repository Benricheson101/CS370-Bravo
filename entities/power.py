from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Power(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(9)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('An increase Whip Power Ring!')
            from level.level_load import game_instance
            if game_instance:
                game_instance.whip_power += 1
                return True
        return False
    
    def update(self, **kwargs):
        return super().update(**kwargs)


