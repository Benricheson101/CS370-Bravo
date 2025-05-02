from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects 


class Forest(Cell):
    """
    A forest. Blocks movement and deducts score if collided with.
    """
    has_paused_message = False
    sound_effects = SoundEffects()  
    def __init__(self) -> None:
        super().__init__()
        self.col(6, 0)
        self.bak(2, 7)
        self.load_dos_char(176)
        self.fast_pc = False
        
    def is_breakable_wall(self): return True

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.BlockSound()
            from level.level_load import game_instance
            if not Forest.has_paused_message:
                game_instance.sm.current_state.pause_flash(14,25,'You cannot travel through forest terrain.')
                Forest.has_paused_message = True
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20

        return False
    
    #Enemies do not suicide into trees; they merely stop.
    #Bombs do not destroy trees.