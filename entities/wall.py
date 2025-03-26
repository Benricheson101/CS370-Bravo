from renderer.cell import Cell


class Wall(Cell):
    def __init__(self, color: int = 6) -> None:
        super().__init__()
        self.col(color, 7)
        self.bak(color, 7)
        self.load_dos_char(219)

    def on_collision(self, cell: Cell) -> bool:
        # prevent moving into the same space
        return False



