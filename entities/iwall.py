from entities.wall import Wall
from renderer.cell import Cell
from entities.player import Player

class IWall(Wall):
    def __init__(self, color: int = 6) -> None:
        super().__init__(color)
        self.image.fill((0, 0, 0, 0))   # for some reason dos_character(0) didn't work here
        self.is_invisible = True  # Track invisibility state

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player) and self.is_invisible:
            self.load_dos_char(219)  # Reveal wall on collision
            self.is_invisible = False
        return False
