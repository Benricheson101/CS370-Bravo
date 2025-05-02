from renderer.cell import Cell
from entities.player import Player
from renderer.cell_grid import CellGrid
from entities.owall1 import OWall1
from Sound import SoundEffects

class OSpell1(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(11,7)
        self.load_dos_char(127)
        
    sound_effects = SoundEffects()
        
    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound(FastPC=True)
            self.destroy_owalls()
            from level.level_load import game_instance
            if not OSpell1.has_paused_message:
                game_instance.sm.current_state.pause_flash(16,25,'Magic has been released in this chamber!')
                OSpell1.has_paused_message = True
        return True

    def on_added_to_grid(self, grid: CellGrid):
        self.grid = grid

    def destroy_owalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, OWall1):
                    self.grid.remove((x, y))  # remove the wall from the grid
