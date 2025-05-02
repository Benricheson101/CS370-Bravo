from entities.wall import Wall
from renderer.cell import Cell
from entities.player import Player
from constants import COLORS
from Sound import SoundEffects

class CWall1(Wall):
    def __init__(self, color: int = 6) -> None:
        super().__init__(color)
        self.color = color
        self.image.fill((0, 0, 0, 0))
        self.is_invisible = True
        
    sound_effects = SoundEffects()

    def reveal(self):
        self.is_invisible = False
        self.image.fill(COLORS[self.color])
        self.load_dos_char(219)
        if self.grid:
            self.grid.group.add(self)
            self.visible = True

    def on_collision(self, cell: Cell) -> bool:
        self.sound_effects.BlockSound(FastPC=True)
        return self.is_invisible  # passable when invisible
