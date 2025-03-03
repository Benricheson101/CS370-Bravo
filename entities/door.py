from constants import (
    MAGENTA,
    CYAN
)
from renderer.cell import Cell


class Door(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(MAGENTA)
        self.load_dos_char(236, CYAN)

    def on_collision(self, cell: Cell) -> bool:
        # prevent moving into the same space
        return False
    

    
