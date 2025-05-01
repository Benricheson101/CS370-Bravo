"""
APPEARANCE:  Red glowing block, sometimes flashing
METADATA:  V
POINT VALUE:  varies by episode; either 1,000 (earlier) or 250 (later).

Lava acts as a barrier to you and enemies, although not an insurmountable one.

Lava is frequently your worst enemy in Kroz games.  Contact with it gives you
lots of points, but it takes 10 gems away.

Despite this profoundly negative consequence, it is often beneficial to cross
lava.  Some passages can only be reached by doing so, and some secret items can
be obtained as well.
"""

from renderer.cell import Cell
from constants import RED
from entities.player import Player


class Lava(Cell):
    def __init__(self):
        super().__init__()
        self.load_dos_char(178, RED)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            self.grid.game.gem_count -= 0 if self.grid.game.gem_count <= 0 else 1
            if self.grid.game.gem_count <= 0:
                cell.dead()
            else:
                return True
        return False
