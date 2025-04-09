from entities.player import Player
from renderer.cell import Cell
from screens.game import load_current_level

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

            grid = self.grid
            # Clear current level display
            grid.clrscr()
            grid.border()
            

            # Load the next level using game's method
            load_current_level(self)

            print("To the next level!")
            return False

        return False


