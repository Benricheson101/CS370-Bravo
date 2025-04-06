from pygame import Color
from constants import LIGHTCYAN
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects 


class Gem(Cell):
    
    sound_effects = SoundEffects()
    
    def __init__(self, color: Color) -> None:
        super().__init__()
        # self.col(self.grid.game.gem_color if self.grid is not None and self.grid.game is not None else LIGHTCYAN, 7)
        self.col(color, 7)
        self.load_dos_char(4)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Gem!")
            
            #Gem.sound_effects.play_sound_in_thread(Gem.sound_effects.grab_sound)
            
            from level.level_load import game_instance
            if game_instance:
                game_instance.gem_count += 1
                return True
        return False


    def update(self, **kwargs):
        return super().update(**kwargs)
