from entities.ospell1 import OSpell1  # Inherit from OSpell1
from entities.owall2 import OWall2

class OSpell2(OSpell1):
    def destroy_owalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, OWall2):
                    self.grid.remove((x, y))
