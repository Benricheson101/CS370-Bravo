from entities.ospell1 import OSpell1  # Inherit from OSpell1
from entities.owall3 import OWall3

class OSpell3(OSpell1):
    def destroy_owalls(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                entity = self.grid.at((x, y))
                if isinstance(entity, OWall3):
                    self.grid.remove((x, y))