from constants import (
    LIGHTGRAY,
    BLACK
)
from entities.player import Player
from renderer.cell import Cell

class Stairs(Cell):
    def __init__(self) -> None:
        super().__init__()
        # self.img.fill(LIGHTGRAY)
        self.image.fill(LIGHTGRAY)
        self.load_dos_char(240, BLACK)
        self.blink = True

    def on_collision(self, cell: "Cell") -> bool:
        from level.level_load import (
            del_level,
            load_level,
            increase_level_num
        )
        if isinstance(cell, Player):
            del_level()
            load_level(increase_level_num())
            print("To the next level!")
            return False

        return False
