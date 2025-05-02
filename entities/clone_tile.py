from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from entities.clone import Clone

def spawn_random_player(grid: CellGrid):
    x, y = grid.get_random_empty_tiles()
    grid.put((x, y), Clone())

class CloneTile(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(2, 7)
        self.load_dos_char(21)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player) and self.grid:
            print('Wow, you just cloned yourself!')
            spawn_random_player(self.grid)
        
            return True
        return False

