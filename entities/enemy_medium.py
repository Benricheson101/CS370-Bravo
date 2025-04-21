'''
OBJECT:  Green enemy
APPEARANCE:  Green "O" with umlaut; various other appearances
METADATA:  2
POINT VALUE:  20

The level-2 enemy moves at medium speed
'''

from typing import Optional
from constants import GREEN
from entities.player import Player
from renderer.cell import Cell
from gameState import is_frozen
import pygame


class Enemy_Medium(Cell):
    def __init__(self, player: Optional[Player] = None) -> None:
        super().__init__()
        self.col(10, 7)
        self.load_dos_char(153)
        self.speed = 2
        self.player = player  # Store player reference
        self.last_move_time = pygame.time.get_ticks()  # Milliseconds

    def is_enemy(self): return True

    def update(self, **kwargs) -> None:
        assert self.grid and self.grid.game
        if self.player is None:
            self.player = self.grid.game.player

        if self.player is None:
            print("Player is still None in enemy update!")
            return

        current_time = pygame.time.get_ticks()

        # Move every 1000 milliseconds (1 second)
        if current_time - self.last_move_time < 2000:
            return

        self.last_move_time = current_time

        if is_frozen():
            return


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
