from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects 


class Wall(Cell):
    has_paused_message = False
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
            self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
            from level.level_load import game_instance
            if not Wall.has_paused_message:
                game_instance.sm.current_state.pause_flash(20,25,'A Solid Wall blocks your way.')
                Wall.has_paused_message = True
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        return False



