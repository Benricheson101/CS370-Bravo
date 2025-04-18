from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects 


class Block(Cell):
    """
    A crumbled wall. For some reason the pascal code calls it "Block"
    """
    sound_effects = SoundEffects()  # Initialize the sound effects
    def __init__(self) -> None:
        super().__init__()
        self.col(6,7)
        self.load_dos_char(178)
        #SOUND
        self.fast_pc = False
        
    def is_breakable_wall(self): return True

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('A Crumbled Wall blocks your way.')
            self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
            from level.level_load import game_instance
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
        return False
