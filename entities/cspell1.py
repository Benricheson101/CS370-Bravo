from entities.wall import Wall
from renderer.cell import Cell
from entities.player import Player
from renderer.cell_grid import CellGrid
from entities.cwall1 import CWall1

def create_walls(self, grid: CellGrid):
    for cwall in grid:
        return True

# def create_walls(grid: CellGrid):
#     for _ in range(20):
#         x, y = grid.get_random_empty_tiles()
#         from level.level_load import game_instance
#         grid.put((x, y), Gem(game_instance.gem_color))

class CSpell1(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(0)

    def on_collision(self, cell: Cell) -> bool:
        # if isinstance(cell, Player):
            
        return True
