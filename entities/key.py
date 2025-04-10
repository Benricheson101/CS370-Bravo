from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell



class Key(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(12,15)
        self.load_dos_char(140)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('Use Keys to unlock doors.')
            from level.level_load import game_instance
            if game_instance:
                game_instance.key_count += 1
            return True
        return False



