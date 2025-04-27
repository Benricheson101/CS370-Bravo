from constants import LIGHTMAGENTA
from entities.player import Player
from renderer.cell import Cell


class Teleport(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(13,7)
        self.load_dos_char(24)

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        if isinstance(cell, Player):
            from level.level_load import game_instance
            if game_instance:
                game_instance.teleport_count += 1
                game_instance.score += 10
                print(f"Whip count: {game_instance.teleport_count}")
            return True
        return False
