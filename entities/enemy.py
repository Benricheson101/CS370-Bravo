from typing import Optional
from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects
from gameState import is_frozen
import pygame

class Enemy(Cell):
    def __init__(self, player: Optional[Player] = None) -> None:
        super().__init__()
        self.load_dos_char(142, LIGHTRED)
        self.speed = 2
        self.player = player  # Store player reference
        self.last_move_time = pygame.time.get_ticks()  # Milliseconds
        
    def is_enemy(self): return True

    def update(self, **kwargs) -> None:
        if self.player is None:
            print("Player is still None in enemy update!")
            return
        
        current_time = pygame.time.get_ticks()

        # Move every 1000 milliseconds (1 second)
        if current_time - self.last_move_time < 2500:
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
            from level.level_load import game_instance
            
            if game_instance.gem_count > 0:
                if game_instance:  
                    game_instance.gem_count -= 1
                return True
            
        return False

