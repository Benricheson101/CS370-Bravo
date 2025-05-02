import pygame
from renderer.cell import Cell
from constants import YELLOW, BROWN
from entities.player import Player
from Sound import SoundEffects

class KLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(75)
        
    sound_effects = SoundEffects()
        
    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound()
            from level.level_load import game_instance
            if game_instance:
                game_instance.score += 2000
                print (game_instance.score)
                return True
        return False


class RLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(82)
        
    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
        
            #self.sound_effects.play_in_thread(self.sound_effects.GrabSound, self.fast_pc)
        
            from level.level_load import game_instance
            if game_instance:
                game_instance.score += 2000
                return True
        return False


class OLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(79)
        
    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
        
            #self.sound_effects.play_in_thread(self.sound_effects.GrabSound, self.fast_pc)
        
            from level.level_load import game_instance
            if game_instance:
                game_instance.score += 2000
                return True
        return False


class ZLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(90)
        
    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
        
            #self.sound_effects.play_in_thread(self.sound_effects.GrabSound, self.fast_pc)
        
            from level.level_load import game_instance
            if game_instance:
                game_instance.score += 2000
                return True
        return False
