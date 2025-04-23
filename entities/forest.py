from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects 


class Forest(Cell):
    """
    A forest. Blocks movement and deducts score if collided with.
    """
    #sound_effects = SoundEffects()  # Initialize the sound effects
    def __init__(self) -> None:
        super().__init__()
        #Forest
        
        self.col(6, 0)
        self.bak(2, 7)
        self.load_dos_char(176)
        #SOUND
        self.fast_pc = False
        
    def is_breakable_wall(self): return True

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('A Forrest blocks your way.')
            #self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
            from level.level_load import game_instance
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
                    
        #self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
        return False
    
    #Enemies do not suicide into trees; they merely stop.
    #Bombs do not destroy trees.