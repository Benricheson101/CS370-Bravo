from renderer.cell import Cell
from Sound import SoundEffects 
from entities.player import Player


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

    def on_collision(self, cell: "Cell") -> bool:
        self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
        if isinstance(cell, Player):
            print('A Crumbled Wall blocks your way.')
            from level.level_load import game_instance
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        return False
