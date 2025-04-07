'''
OBJECT:  Freeze time spell
APPEARANCE:  Light blue f
METADATA:  Z
POINT VALUE:  20 or 10

When picked up, enemies will stop their movement rate for a brief period.
'''

from pygame import Color
from constants import LIGHTBLUE
from entities.player import Player
from renderer.cell import Cell
from gameState import freeze_enemies_for


class Spell_Freeze(Cell):
    def __init__(self):
        super().__init__()
        self.load_dos_char(102, LIGHTBLUE)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Freeze Scroll!")
            freeze_enemies_for(10000)
            return True
        
        return False

    def update(self, **kwargs):
        return super().update(**kwargs)
