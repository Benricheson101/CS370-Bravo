from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects

class Power(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(9)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound()
            from level.level_load import game_instance
            if not Power.has_paused_message:
                game_instance.sm.current_state.pause_flash(22,25,'An increase Whip Power Ring!')
                Power.has_paused_message = True
            if game_instance:
                game_instance.whip_power += 1
                return True
        return False
    
    def update(self, **kwargs):
        return super().update(**kwargs)


