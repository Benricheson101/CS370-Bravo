'''
OBJECT:  Blue enemy
APPEARANCE:  Blue omega; various other appearances
METADATA:  3
POINT VALUE:  30

The level-3 enemy moves fast
'''

from entities.enemy import Enemy


class Enemy_Hard(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.col(9, 7)
        self.load_dos_char(234)
        self.speed = 2.5
        self.move_time = 1000
