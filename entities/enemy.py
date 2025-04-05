from typing import Optional
from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
import pygame


class Enemy(Cell):
    def __init__(self, player: Optional[Player] = None) -> None:
        super().__init__()
        self.load_dos_char(142, LIGHTRED)
        # _josh changed the speed
        self.speed = 2.5
        self.player = player  # Store player reference

    def update(self, **kwargs) -> None:
        if not self.grid:
            print("Enemy is not assigned to a grid!")
            return
        
        if self.player is None:
            print("Player is still None in enemy update!")
            return

        player_pos = pygame.Vector2(self.player.get_player_position())
        enemy_pos = pygame.Vector2(self.x, self.y)
        
        print(f"Enemy at {enemy_pos}, Player at {player_pos}")  # Debug print

        
        direction = player_pos - enemy_pos
        if direction.length() > 0:
            direction = direction.normalize()
            self.move(direction * self.speed)
            print(f"Enemy moved to {self.x, self.y}")  # Debug print after move


    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a monster! OUCHIE!")
            return True

        return False