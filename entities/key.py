from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects



class Key(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(12,15)
        self.load_dos_char(140)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound(FastPC=True)
            print('Use Keys to unlock doors.')
            from level.level_load import game_instance
            if not Key.has_paused_message:
                game_instance.sm.current_state.pause_flash(22,25,'Use Keys to unlock doors.')
                Key.has_paused_message = True
            if game_instance:
                game_instance.key_count += 1
            return True
        return False



