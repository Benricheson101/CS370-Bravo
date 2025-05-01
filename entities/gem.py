from pygame import Color
from constants import LIGHTCYAN
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects 


class Gem(Cell):
    has_paused_message = False
    sound_effects = SoundEffects()
    
    def __init__(self, color: Color) -> None:
        super().__init__()
        # self.col(self.grid.game.gem_color if self.grid is not None and self.grid.game is not None else LIGHTCYAN, 7)
        self.col(color, 7)
        self.load_dos_char(4)
        self.fast_pc = False

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Gem!")
            
            self.sound_effects.play_in_thread(self.sound_effects.GrabSound, self.fast_pc)
            
            from level.level_load import game_instance
            if not Gem.has_paused_message:
                game_instance.sm.current_state.pause_flash(15,25,'Gems give you both points and strength.')
                Gem.has_paused_message = True
            if game_instance:
                game_instance.gem_count += 1
                game_instance.score += 10
                return True
        return False


    def update(self, **kwargs):
        return super().update(**kwargs)
