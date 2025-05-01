from entities.cspell1 import CSpell1  # Inherit from CSpell1
from entities.cwall2 import CWall2

class CSpell2(CSpell1):
    def reveal_cwalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, CWall2) and entity.is_invisible:
                    entity.reveal()
