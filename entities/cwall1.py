from entities.wall import Wall
from renderer.cell import Cell
from entities.player import Player



class CWall1(Wall):
    def __init__(self, color: int = 6) -> None:
        super().__init__(color)
        self.image.fill((0, 0, 0, 0))   # for some reason dos_character(0) didn't work here
        self.is_invisible = True 
        
    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player) and self.is_invisible:
            return True
    
    def get_cwall_position(self) -> tuple[int, int]:
        return self.x, self.y
    
    
    
    