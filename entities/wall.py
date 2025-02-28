from constants import ORANGE
from renderer.cell import Cell


class Wall(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(ORANGE)
        self.load_dos_char(219, ORANGE)

    def on_collision(self, cell: Cell) -> bool:
        # prevent moving into the same space
        return False
