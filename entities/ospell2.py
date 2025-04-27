from renderer.cell import Cell
from entities.player import Player
from renderer.cell_grid import CellGrid
from entities.owall2 import OWall2

class OSpell2(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(127)
        self.col(11,7)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.destroy_owalls()
        return True

    def on_added_to_grid(self, grid: CellGrid):
        self.grid = grid

    def destroy_owalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, OWall2):
                    self.grid.remove((x, y))  # remove the wall from the grid
