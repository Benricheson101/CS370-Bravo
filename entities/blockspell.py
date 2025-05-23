from renderer.cell import Cell
from entities.player import Player
from renderer.cell_grid import CellGrid
from entities.zblock import ZBlock
from Sound import SoundEffects

class BlockSpell(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(0)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound(FastPC=True)
            self.destroy_owalls()
            from level.level_load import game_instance
            if not BlockSpell.has_paused_message:
                game_instance.sm.current_state.pause_flash(19,25,'You''ve triggered a secret area.')
                BlockSpell.has_paused_message = True
        return True

    def on_added_to_grid(self, grid: CellGrid):
        self.grid = grid

    def destroy_owalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, ZBlock):
                    self.grid.remove((x, y))  # remove the wall from the grid
