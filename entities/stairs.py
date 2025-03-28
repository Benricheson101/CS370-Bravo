from entities.player import Player
from renderer.cell import Cell

class Stairs(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.bak(7, 7)
        self.col(16, 16)
        self.load_dos_char(240)

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid
        assert self.grid.game

        if isinstance(cell, Player):
            # Increment the level number
            self.grid.game.current_level += 1

            # Clear the current level
            self.grid.game.game_grid.clrscr()
            self.grid.game.game_grid.border()

            # Load the next level using load_current_level()
            self.grid.game.load_current_level()

            print("To the next level!")
            return False

        return False
