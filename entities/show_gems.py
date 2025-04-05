from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from entities.gem import Gem
from typing import Optional
import pygame

# amount of gems shown should be (Difficulty * 2) + 5
def show_gems(grid: CellGrid):
    for _ in range(20):
        x, y = grid.get_random_empty_tiles()
        grid.put((x, y), Gem(LIGHTRED))


class ShowGems(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.grid: Optional[CellGrid] = None # for show_gems function
        self.load_dos_char(0)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player) and self.grid:
            print('Yah Hoo! You discovered a hidden Reveal Gems Scroll!')
            show_gems(self.grid)
            return True
        return False
