from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects 


class Tree(Cell):
    """
    A forest. Blocks movement and deducts score if collided with.
    """
    has_paused_message = False
    #sound_effects = SoundEffects()  # Initialize the sound effects
    def __init__(self) -> None:
        super().__init__()
        #Tree
        
        self.col(6, 0)
        self.bak(2, 6)
        self.load_dos_char(177)
        #SOUND
        self.fast_pc = False
        
    def is_breakable_wall(self): return True

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            #self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
            from level.level_load import game_instance
            if not Tree.has_paused_message:
                game_instance.sm.current_state.pause_flash(24,25,'A tree blocks your way.')
                Tree.has_paused_message = True
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
                    
        #self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
        return False
    
    #Enemies do not suicide into trees; they merely stop.
    #Bombs do not destroy trees.