from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Crown(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 15)
        self.load_dos_char(5)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('The Crown is finally yours--25,000 points!')
            from level.level_load import game_instance
            if game_instance:
                game_instance.score += 25000
                return True
        return False


