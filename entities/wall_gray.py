from constants import LIGHTGRAY
from entities.wall import Wall

# called OWall3 in the pascal code
class WallGray(Wall):
    def __init__(self) -> None:
        super().__init__(7)
