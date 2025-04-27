from pygame import Color
from constants import LIGHTGRAY
from entities.player import Player
from renderer.cell import Cell

class Clone(Player):
    def __init__(self) -> None:
        super().__init__()
        self.col(2, 7)  # Make the clone green
        self.clone = True

    def use_whip(self) -> None:
        """Prevent clone from whipping."""
        pass  # Disable whip usage

    def on_collision(self, cell: "Cell") -> bool:
        from entities.enemy import Enemy
        from entities.lava import Lava
        
        if isinstance(cell, (Enemy, Lava)):
            if self.grid:
                print("Clone removed!")
                self.grid.remove((self.x, self.y))
            return True

        return super().on_collision(cell)

