from constants import ORANGE
from renderer.cell import Cell


class WallTile(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(ORANGE)
        self.walkable = False

