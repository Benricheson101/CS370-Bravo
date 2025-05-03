from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from entities.clone import Clone

def spawn_random_player(grid: CellGrid):
    x, y = grid.get_random_empty_tiles()
    grid.put((x, y), Clone())

class CloneTile(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(2, 7)
        self.load_dos_char(21)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player) and self.grid:
            spawn_random_player(self.grid)
            from level.level_load import game_instance
            if not CloneTile.has_paused_message:
                game_instance.sm.current_state.pause_flash(18,25,'Wow, you just cloned yourself!')
                CloneTile.has_paused_message = True
        
            return True
        return False

