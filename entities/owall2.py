from entities.wall import Wall
from renderer.cell import Cell
from entities.player import Player
from constants import COLORS

class OWall2(Wall):
    def __init__(self, color: int = 6) -> None:
        super().__init__(color)
        self.color = color
        self.image.fill(COLORS[self.color])
        self.load_dos_char(219)

    def on_collision(self, cell: Cell) -> bool:
        return False
