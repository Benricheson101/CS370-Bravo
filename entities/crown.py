from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Crown(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 15)
        self.load_dos_char(5)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('The Crown is finally yours--25,000 points!')
            from level.level_load import game_instance
            if not Crown.has_paused_message:
                sm = game_instance.sm
                sm.current_state.pause(True)
                self.grid.flash(13,25,'The Crown is finally yours--25,000 points!')
                sm.current_state.pause_reason = "crown"
                Crown.has_paused_message = True
            if game_instance:
                game_instance.score += 25000
                return True
        return False


