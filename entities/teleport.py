from constants import LIGHTMAGENTA
from entities.player import Player
from renderer.cell import Cell


class Teleport(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(13,7)
        self.load_dos_char(24)
        self.collected = False

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        if isinstance(cell, Player) and not self.collected:
            print("Player collected a Teleport scroll!")
            self.collected = True
            self.grid.remove((self.x, self.y))  # Remove it from the grid
            cell.collected_teleports += 1       # Increment player's teleport count
            return True
        return False
