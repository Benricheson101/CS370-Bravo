from renderer.cell import Cell


class Border(Cell):
    def __init__(self, fg: int, bg: int) -> None:
        super().__init__()
        self.col(fg, 0)
        self.bak(bg, 7)
        self.blink = False
        self.load_dos_char(178)

    def on_collision(self, cell: "Cell") -> bool:
        # TODO: player hit a wall so remove points or whatever. and show flashing text
        return False
