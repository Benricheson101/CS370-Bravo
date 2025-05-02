from pygame import Surface, Color
from constants import LIGHTGREEN
from entities.player import Player
from renderer.cell import Cell
from random import randint

class Clone(Player):
    def __init__(self) -> None:
        super().__init__()

        self.clone = True

        # Redefine the appearance
        rand1 = randint(0,255) 
        rand2 = randint(0,255)
        rand3 = randint(0,255)
        self.fg = (Color(rand1, rand2, rand3), Color(rand1, rand2, rand3))  # green in color & monochrome
        self.bg = (Color(0, 0, 0, 0), Color(0, 0, 0, 0))  # transparent background

        # Recreate the visual appearance
        self.load_dos_char(2)  # Re-load the same DOS char but with new fg/bg

    def use_whip(self) -> None:
        """Prevent clone from whipping."""
        pass
    
    
    def on_collision(self, cell: "Cell") -> bool:
        from entities.enemy import Enemy
        if isinstance(cell, Enemy):
            return False  # Clone doesn't die to enemies
        if isinstance(cell, Player):
            return False  # Clone doesn't collide with Player
        else:
            return True


