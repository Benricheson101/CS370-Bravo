import random
import pygame
from constants import WHITE
from entities.player import Player
from renderer.cell import Cell
# from level.level_load import game_instance

#for WhipFlash
from entities.char import Char

class Whip(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(244)
    
    def on_collision(self, cell: "Cell") -> bool:
        
        if isinstance(cell, Player):
            self.sound_effects.play_in_thread(self.sound_effects.GrabSound, self.fast_pc)
            from level.level_load import game_instance
            if not Whip.has_paused_message:
                game_instance.sm.current_state.pause_flash(26,25,'You found a Whip.')
                Whip.has_paused_message = True
            if game_instance:
                game_instance.whip_count += 1
                game_instance.score += 10
                return True
            return True
        return False
    
# for Whip animation
class WhipFlash(Char):
    def __init__(self, symbol: str, grid, pos, duration=150):
        from constants import TRANSPARENT
        super().__init__(symbol, fg=pygame.Color("white"), bg=TRANSPARENT, blink=True)

        self.grid = grid
        self.x, self.y = pos
        self.rect.topleft = (self.x * grid.cell_width, self.y * grid.cell_height)
        self.visible = True
        self.expire_time = pygame.time.get_ticks() + duration

    def update(self, **kwargs):
        super().update(**kwargs)
        if pygame.time.get_ticks() >= self.expire_time:
            self.grid.fx_group.remove(self)
    