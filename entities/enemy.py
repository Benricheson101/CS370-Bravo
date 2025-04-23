from typing import Optional
from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell
from Sound import SoundEffects
from gameState import is_frozen
from entities.tree import Tree
from entities.forest import Forest
import pygame

class Enemy(Cell):
    def __init__(self, player: Optional[Player] = None) -> None:
        super().__init__()
        self.col(12, 7)
        self.load_dos_char(142)
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
        if isinstance(cell, Player):
            print("Player hit a monster! OUCHIE!")
            from level.level_load import game_instance

            if game_instance.gem_count > 0:
                if game_instance:
                    game_instance.gem_count -= 1
                return True
            else:
                cell.dead()
            
        return False

