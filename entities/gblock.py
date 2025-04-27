from entities.block import Block

class GBlock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.col(7, 7)
        self.load_dos_char(178)