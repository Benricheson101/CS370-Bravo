from constants import BROWN
from renderer.cell import Cell


class Wall(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(BROWN)
        self.load_dos_char(219, BROWN)

    def on_collision(self, cell: Cell) -> bool:
        # prevent moving into the same space
        return False
