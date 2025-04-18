from renderer.cell import Cell
from entities.player import Player
from renderer.cell_grid import CellGrid
from entities.cwall1 import CWall1

class CSpell1(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(0)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.reveal_cwalls()
        return True

    def on_added_to_grid(self, grid: CellGrid):
        self.grid = grid

    def reveal_cwalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, CWall1) and entity.is_invisible:
                    entity.reveal()
