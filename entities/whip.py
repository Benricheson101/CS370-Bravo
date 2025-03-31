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
        from level.level_load import game_instance
        if isinstance(cell, Player):
            print("Picked up a whip!")
            game_instance.whip_count += 1
            print(f"Whip count: {game_instance.whip_count}")
            return True
        return False
    
    def use_whip(self):
        from level.level_load import game_instance
        if game_instance.whip_count > 0:
            game_instance.whip_count -= 1
            print(f"Whip used! Remaining whips: {game_instance.whip_count}")
            # Play whip sound effect
            return True
        print("No whips left!")
        return False
    
    def activate(self):
        from level.level_load import game_instance
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.use_whip():
                px, py = game_instance.player.x, game_instance.player.y
                hits = [
                    (px - 1, py - 1, '\\'),  # Top-left
                    (px - 1, py, 'ƒ'),       # Left
                    (px - 1, py + 1, '/'),   # Bottom-left
                    (px, py + 1, '≥'),       # Down
                    (px + 1, py + 1, '\\'),  # Bottom-right
                    (px + 1, py, 'ƒ'),       # Right
                    (px + 1, py - 1, '/'),   # Top-right
                    (px, py - 1, '≥')        # Up
                ]
                for x, y, symbol in hits:
                    self.process_hit(x, y, symbol)
    
    #def process_hit(self, x, y, symbol):
        #from level.level_load import game_instance 
        #cell = game_instance.get_cell(x, y)
        #if cell:

    #TODO: get player count of whips
        #button to use whip
        #in use whip function, have whip spin around
        #if whip hits enemy, it dies
        #if whip hits wall, chance for wall to break


