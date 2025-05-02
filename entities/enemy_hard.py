'''
OBJECT:  Blue enemy
APPEARANCE:  Blue omega; various other appearances
METADATA:  3
POINT VALUE:  30

The level-3 enemy moves fast
'''
from typing import Optional
from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects
from gameState import is_frozen
from entities.tree import Tree
from entities.forest import Forest
import pygame
from entities.enemy import Enemy



class Enemy_Hard(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.col(9, 7)
        self.load_dos_char(234)
        self.speed = 2.5
        self.move_time = 1000
        
    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid and self.grid.game

        if isinstance(cell, Player):
            # from level.level_load import game_instance

            # if game_instance.gem_count > 0:
            self.grid.game.gem_count -= 0 if self.grid.game.gem_count <= 0 else 3
            if self.grid.game.gem_count <= 0:
                cell.dead()
            else:
                return True

        return False
