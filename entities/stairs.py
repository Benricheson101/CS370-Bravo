from entities.player import Player
from renderer.cell import Cell

class Stairs(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.bak(7, 7)
        self.col(16, 16)
        self.load_dos_char(240)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            from level.level_load import game_instance
            if not Stairs.has_paused_message:
                game_instance.sm.current_state.pause_flash(14,25,'Stairs take you to the next lower level.')
                Stairs.has_paused_message = True
                return True # first stairs entity just does pause_flash
            game = self.grid.game

            # Increment the level number
            game.current_level += 1

            grid = self.grid
            game_screen = self.grid.game.sm.current_state
            # Clear current level display
            grid.clrscr()
            grid.border()


            # Load the next level using game's method
            game_screen.load_current_level()

            game_instance.sm.current_state.enter()
            return False

        return False


