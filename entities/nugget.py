from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects

class Nugget(Cell):
    has_paused_message = False
    def __init__(self, color: Color) -> None:
        super().__init__()
        self.col(color, 7)
        self.load_dos_char(15)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound(FastPC=True)
            from level.level_load import game_instance
            if not Nugget.has_paused_message:
                game_instance.sm.current_state.pause_flash(15,25,'You found a Gold Nugget...500 points!')
                Nugget.has_paused_message = True
            if game_instance:
                game_instance.score += 500
                return True
        return False
    
    def update(self, **kwargs):
        return super().update(**kwargs)


