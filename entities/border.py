from renderer.cell import Cell
from Sound import SoundEffects



class Border(Cell):
    has_paused_message = False
    def __init__(self, fg: int, bg: int) -> None:
        super().__init__()
        self.col(fg, 0)
        self.bak(bg, 7)
        self.blink = False
        self.load_dos_char(178)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        from entities.player import Player
        if isinstance(cell, Player):
            self.sound_effects.BlockSound()
            from level.level_load import game_instance
            if not Border.has_paused_message:
                game_instance.sm.current_state.pause_flash(16,25,'An electrified Wall blocks your way.')
                Border.has_paused_message = True
                

        return False
