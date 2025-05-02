'''
OBJECT:  Green enemy
APPEARANCE:  Green "O" with umlaut; various other appearances
METADATA:  2
POINT VALUE:  20

The level-2 enemy moves at medium speed
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


class Enemy_Medium(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.col(10, 7)
        self.load_dos_char(153)
        self.speed = 2
        self.move_time = 2000
        
    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid and self.grid.game

        if isinstance(cell, Player):
            # from level.level_load import game_instance

            # if game_instance.gem_count > 0:
            self.grid.game.gem_count -= 0 if self.grid.game.gem_count <= 0 else 2
            if self.grid.game.gem_count <= 0:
                cell.dead()
            else:
                return True

        return False
