from entities.block import Block
from renderer.cell import Cell
from entities.player import Player

class IBlock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill((0, 0, 0, 0))   # for some reason dos_character(0) didn't work here
        self.is_invisible = True  # Track invisibility state

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player) and self.is_invisible:
            self.load_dos_char(178)  # Reveal wall on collision
            self.is_invisible = False
        return False
