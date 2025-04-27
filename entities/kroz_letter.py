import pygame
from renderer.cell import Cell
from constants import YELLOW, BROWN
from entities.player import Player

class KLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.letter = 'K'

class RLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.letter = 'R'

class OLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.letter = 'O'

class ZLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.letter = 'Z'