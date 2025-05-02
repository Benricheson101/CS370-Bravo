from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects

class River(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.bak(1, 7)
        self.col(9, 0)
        self.load_dos_char(247)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.sound_effects.BlockSound()
            from level.level_load import game_instance
            if not River.has_paused_message:
                game_instance.sm.current_state.pause_flash(18,25,'You cannot travel through Water.')
                River.has_paused_message = True
        return False


