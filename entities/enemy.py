from typing import Optional
from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects
from gameState import is_frozen
from entities.tree import Tree
from entities.forest import Forest
import pygame

from util.math import clamped_add 

class Enemy(Cell):    
    def __init__(self) -> None:
        super().__init__()
        self.col(12, 7)
        self.load_dos_char(142)
        self.speed = 2
        self.last_move_time = pygame.time.get_ticks()  # Milliseconds
        self.move_time = 2500

    def is_enemy(self): return True

    def update(self, **kwargs) -> None:
        if not self.grid:
            return  # This enemy was removed

        player = self.grid.game.player
        current_time = pygame.time.get_ticks()

        if current_time - self.last_move_time < self.move_time:
            return

        self.last_move_time = current_time

        if is_frozen():
            return

        player_pos = pygame.Vector2(player.x, player.y)
        enemy_pos = pygame.Vector2(self.x, self.y)

        direction = player_pos - enemy_pos
        if direction.length() > 1:
            direction = direction.normalize()
            self.move(direction * self.speed)
        else:
            self.move_to(player.pos)


    #not sure if this is right kinda asked google about some of it
    '''def move(self, direction_vector):
        # Calculate target position
        target_x = int(self.x + direction_vector.x)
        target_y = int(self.y + direction_vector.y)

        # Check if target cell exists in the grid
        if not self.grid:
            return False

        # Get target cell
        target_cell = self.grid.get_cell_at(target_x, target_y)

        # If target cell is a breakable wall, forest, or tree - stop the enemy
        if target_cell and hasattr(target_cell, 'is_breakable_wall') and target_cell.is_breakable_wall():
            # Enemy stops at the wall without breaking it
            return False

        # For other cells, use the default movement logic
        return super().move(direction_vector)'''

    def on_collision(self, cell: "Cell") -> bool:
        assert self.grid and self.grid.game

        if isinstance(cell, Player):
            # from level.level_load import game_instance

            # if game_instance.gem_count > 0:
            self.grid.game.gem_count -= 0 if self.grid.game.gem_count <= 0 else 1
            if self.grid.game.gem_count <= 0:
                cell.dead()
            else:
                return True

        return False

