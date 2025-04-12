from renderer.cell import Cell
from Sound import SoundEffects 
from entities.player import Player


class Wall(Cell):
    sound_effects = SoundEffects()  # Initialize the sound effects
    def __init__(self, color: int = 6) -> None:
        super().__init__()
        self.col(color, 7)
        self.bak(color, 7)
        self.load_dos_char(219)
        self.fast_pc = False

    def on_collision(self, cell: Cell) -> bool:
        # prevent moving into the same space
        if isinstance(cell, Player):
            print('A Solid Wall blocks your way.')
            self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
            from level.level_load import game_instance
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        return False



