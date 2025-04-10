import random
import pygame
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Whip(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(244)
    
    def on_collision(self, cell: "Cell") -> bool:
        
        if isinstance(cell, Player):
            print('You found a Whip.')
            from level.level_load import game_instance
            if game_instance:
                game_instance.whip_count += 1
                game_instance.score += 10
                return True
        return False
    
    def use_whip(self):
    # Check if player has whips
        keys = pygame.key.get_pressed()
        if self.whip_count > 0:
            self.whip_count -= 1
            print(f"Whip used! Remaining whips: {self.whip_count}")
            for event in pygame.event.get():
            # Get player position
                px, py = self.player.x, self.player.y
                if  event.key == pygame.K.w:
                    # Define the 8 directions
                    hits = [
                        (px - 1, py - 1, '\\'),  # Top-left
                        (px - 1, py, 'ƒ'),      # Left
                        (px - 1, py + 1, '/'),   # Bottom-left
                        (px, py + 1, '≥'),       # Down
                        (px + 1, py + 1, '\\'),  # Bottom-right
                        (px + 1, py, 'ƒ'),      # Right
                        (px + 1, py - 1, '/'),   # Top-right
                        (px, py - 1, '≥')        # Up
                    ]
        
            # Process hits in all directions
                for x, y, symbol in hits:
                    self.process_whip_hit(x, y, symbol)
                    return True
        else:
            print("No whips left!")
            return False

    def process_whip_hit(self, x, y, symbol):
        # Get the cell at the hit location
        cell = self.game_grid.get_cell(x, y)
    
        if cell:
            if hasattr(cell, 'is_enemy') and cell.is_enemy():
                print(f"Enemy at ({x}, {y}) defeated!")
                # Remove the enemy
                # You might need to implement a method for this
                self.game_grid.remove_cell(x, y)
            elif hasattr(cell, 'is_wall') and cell.is_wall():
                # Check if the wall should break (30% chance)
                if random.random() < 0.3:
                    print(f"Wall at ({x}, {y}) broken!")
                    # Break the wall
                    # You might need to implement a method for this
                    self.game_grid.remove_cell(x, y)
        def use_whip(self):
            from level.level_load import game_instance
            if game_instance.whip_count > 0:
                game_instance.whip_count -= 1
                print(f"Whip used! Remaining whips: {game_instance.whip_count}")
                # Play whip sound effect
                return True
            print("No whips left!")
            return False
    
    #def process_hit(self, x, y, symbol):
        #from level.level_load import game_instance 
        #cell = game_instance.get_cell(x, y)
        #if cell:

    #TODO: get player count of whips
        #button to use whip
        #in use whip function, have whip spin around
        #if whip hits enemy, it dies
        #if whip hits wall, chance for wall to break


