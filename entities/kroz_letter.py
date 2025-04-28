import pygame
from renderer.cell import Cell
from constants import YELLOW, BROWN
from entities.player import Player

class KLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(75)
        self.fast_pc = False

class RLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(82)
        self.fast_pc = False

class OLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(79)
        self.fast_pc = False

class ZLetter(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(14, 7)
        self.load_dos_char(90)
        self.fast_pc = False