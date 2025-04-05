from entities.player import Player
from renderer.cell import Cell

class Stairs(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.bak(7, 7)
        self.col(16, 16)
        self.load_dos_char(240)

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        assert self.grid.game

        from level.level_load import (
            del_level,
            load_level,
            increase_level_num
        )

        if isinstance(cell, Player):
            del_level(self.grid.game)
            load_level(self.grid.game, increase_level_num())
            print("To the next level!")
            return False

        return False
