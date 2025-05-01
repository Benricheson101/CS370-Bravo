from renderer.cell import Cell
from entities.player import Player
from renderer.cell_grid import CellGrid
from entities.zblock import ZBlock

class BlockSpell(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(0)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.destroy_owalls()
            from level.level_load import game_instance
            if not BlockSpell.has_paused_message:
                sm = game_instance.sm
                sm.current_state.pause(True)
                self.grid.flash(19,25,'You''ve triggered a secret area.')
                sm.current_state.pause_reason = "blockspell"
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
