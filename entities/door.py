from constants import (
    MAGENTA,
    CYAN
)
from renderer.cell import Cell
from entities.player import Player

class Door(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.bak(5,7)
        self.col(3,0)
        self.load_dos_char(236)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            from level.level_load import game_instance
            if game_instance:
                if game_instance.key_count > 0:
                    # no message appears when unlocking door
                    # print("You unlocked a Door!")
                    game_instance.key_count -=1
                    game_instance.score += 10
                    return True
                else:
                    return False



