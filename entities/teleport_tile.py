from constants import LIGHTMAGENTA
from entities.player import Player
from renderer.cell import Cell


class Teleport_Tile(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(13,7)
        self.load_dos_char(25)

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        if isinstance(cell, Player):
            print("Player hit a Teleport tile!")
            from level.level_load import game_instance
            if game_instance:
                game_instance.teleport_count += 1

            empty_cell = cell.grid.get_random_empty_tiles()

            cell.move_to((empty_cell))
            self.grid.remove((self.x, self.y))
            game_instance.teleport_count -= 1

            return False

        return False