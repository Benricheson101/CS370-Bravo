from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Nugget(Cell):
    def __init__(self, color: Color) -> None:
        super().__init__()
        self.col(color, 7)
        self.load_dos_char(15)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('You found a Gold Nugget...500 points!')
            from level.level_load import game_instance
            if game_instance:
                game_instance.score += 500
                return True
        return False
    
    def update(self, **kwargs):
        return super().update(**kwargs)


