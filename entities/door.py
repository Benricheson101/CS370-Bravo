from constants import (
    MAGENTA,
    CYAN
)
from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects

class Door(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.bak(5,7)
        self.col(3,0)
        self.load_dos_char(236)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.sound_effects.BlockSound(FastPC=True)
            from level.level_load import game_instance
            if game_instance:
                if game_instance.key_count > 0:
                    # no message appears when unlocking door
                    game_instance.key_count -=1
                    game_instance.score += 10
                    return True
                else:
                    if not Door.has_paused_message:
                        game_instance.sm.current_state.pause_flash(18,25,'To pass the Door you need a Key.')
                        Door.has_paused_message = True
                    return False



