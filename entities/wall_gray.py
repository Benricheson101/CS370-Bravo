from constants import LIGHTGRAY
from entities.wall import Wall

class WallGray(Wall):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(LIGHTGRAY)

    

    
