'''
OBJECT:  Green enemy
APPEARANCE:  Green "O" with umlaut; various other appearances
METADATA:  2
POINT VALUE:  20

The level-2 enemy moves at medium speed
'''

from entities.enemy import Enemy


class Enemy_Medium(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.col(10, 7)
        self.load_dos_char(153)
        self.speed = 2
        self.move_time = 2000
