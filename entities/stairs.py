from entities.player import Player
from renderer.cell import Cell

class Stairs(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.bak(7, 7)
        self.col(16, 16)
        self.load_dos_char(240)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            game = self.grid.game

            # Increment the level number
            game.current_level += 1

            # Clear current level display
            game.game_grid.clrscr()
            game.game_grid.border()

            # Load the next level using game's method
            game.load_current_level()

            print("To the next level!")
            return False

        return False


