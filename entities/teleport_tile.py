from constants import LIGHTMAGENTA
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects


class Teleport_Tile(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(7,7)
        self.load_dos_char(249)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        if isinstance(cell, Player):
            self.sound_effects.GrabSound()
            from level.level_load import game_instance
            if not Teleport_Tile.has_paused_message:
                game_instance.sm.current_state.pause_flash(19,25,'You activated a Teleport trap!')
                Teleport_Tile.has_paused_message = True
            if game_instance:
                game_instance.teleport_count += 1

            empty_cell = cell.grid.get_random_empty_tiles()

            cell.move_to((empty_cell))
            self.grid.remove((self.x, self.y))
            game_instance.teleport_count -= 1

            return False

        return False