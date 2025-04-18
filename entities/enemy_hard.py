'''
OBJECT:  Blue enemy
APPEARANCE:  Blue omega; various other appearances
METADATA:  3
POINT VALUE:  30

The level-3 enemy moves fast
'''

from typing import Optional
from constants import BLUE
from entities.player import Player
from renderer.cell import Cell
import pygame
from gameState import is_frozen


class Enemy_Hard(Cell):
    def __init__(self, player: Optional[Player] = None) -> None:
        super().__init__()
        self.load_dos_char(234, BLUE)
        self.speed = 2.5
        self.player = player  # Store player reference
        self.last_move_time = pygame.time.get_ticks()  # Milliseconds
        
    def is_enemy(self): return True

    def update(self, **kwargs) -> None:
        if not self.grid:
            print("Enemy is not assigned to a grid!")
            return
        
        if self.player is None:
            print("Player is still None in enemy update!")
            return
        
        current_time = pygame.time.get_ticks()

        # Move every 1000 milliseconds (1 second)
        if current_time - self.last_move_time < 1000:
            return
        
        if is_frozen():
            return

        self.last_move_time = current_time


        player_pos = pygame.Vector2(self.player.get_player_position())
        enemy_pos = pygame.Vector2(self.x, self.y)

        
        direction = player_pos - enemy_pos
        if direction.length() > 0:
            direction = direction.normalize()
            self.move(direction * self.speed)


    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a monster! OUCHIE!")
            return True

        return False