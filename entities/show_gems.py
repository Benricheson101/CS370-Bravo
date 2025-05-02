from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from entities.gem import Gem
from typing import Optional
import pygame
from Sound import SoundEffects


# amount of gems shown should be (Difficulty * 2) + 5
def show_gems(grid: CellGrid):
    for _ in range(20):
        x, y = grid.get_random_empty_tiles()
        from level.level_load import game_instance
        grid.put((x, y), Gem(game_instance.gem_color))


class ShowGems(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.grid: Optional[CellGrid] = None # for show_gems function
        self.load_dos_char(0)
    sound_effects = SoundEffects()
    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player) and self.grid:
            show_gems(self.grid)
            self.sound_effects.GrabSound(FastPC=True)
            from level.level_load import game_instance
            if not ShowGems.has_paused_message:
                game_instance.sm.current_state.pause_flash(8,25,'Yah Hoo! You discovered a hidden Reveal Gems Scroll!')
                ShowGems.has_paused_message = True
            return True
        return False
