from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects

class Invisible(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(2, 7)
        self.load_dos_char(173)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound(FastPC=True)
            from level.level_load import game_instance
            if not Invisible.has_paused_message:
                game_instance.sm.current_state.pause_flash(16,25,'Oh no, a temporary Blindness Potion!')
                Invisible.has_paused_message = True
            cell.make_invisible(3000)
        
            return True
        return False

