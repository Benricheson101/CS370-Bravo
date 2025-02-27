from constants import ORANGE
from renderer.cell import Cell


class Block(Cell):
    """
    A crumbled wall. For some reason the pascal code calls it "Block"
    """
    def __init__(self) -> None:
        super().__init__()
        self.load_dos_char(178, ORANGE)

    def on_collision(self, cell: "Cell") -> bool:
        return False
