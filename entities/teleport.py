from constants import LIGHTMAGENTA
from entities.player import Player
from renderer.cell import Cell


class Teleport(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(13,7)
        self.load_dos_char(24)

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        if isinstance(cell, Player):
            self.sound_effects.play_in_thread(self.sound_effects.GrabSound, self.fast_pc)
            from level.level_load import game_instance
            if not Teleport.has_paused_message:
                game_instance.sm.current_state.pause_flash(20,25,'You found a Teleport scroll.')
                Teleport.has_paused_message = True
            if game_instance:
                game_instance.teleport_count += 1
                game_instance.score += 10
            return True
        return False
