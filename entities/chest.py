import random
from pygame import Color
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects

class Chest(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.bak(4,7)
        self.col(14,7)
        self.load_dos_char(67)
        
    sound_effects = SoundEffects()
           
    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('You stumbled across a Chest.')
            self.sound_effects.chest_opening_sound()
            from level.level_load import game_instance
            if game_instance:
                
                game_instance.whip_count = random.randint(2,4)
                game_instance.gem_count = random.randint(2, game_instance.difficulty + 1)
                
                return True
        return False
    
    def update(self, **kwargs):
        return super().update(**kwargs)