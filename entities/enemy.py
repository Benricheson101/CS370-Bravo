from constants import RED
from entities.player import Player
from renderer.cell import Cell


class Enemy(Cell):
    def __init__(self) -> None:
        super().__init__()
        # self.load_sprite("./sprites/enemy.png")
        self.load_dos_char(142, RED)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a monster! OUCHIE!")
            return True

        return False
