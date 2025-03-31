from constants import LIGHTRED
from entities.player import Player
from renderer.cell import Cell


class Enemy(Cell):
    def __init__(self) -> None:
        super().__init__()
        # self.load_sprite("./sprites/enemy.png")
        self.col(12, 7)
        self.load_dos_char(142)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a monster! OUCHIE!")
            from level.level_load import game_instance
            if game_instance.gem_count > 0:
                if game_instance:  
                    game_instance.gem_count -= 1
                return True
        return False

    #TODO Make chase function:
        #get player position
        #compare y
        # move towards player on y axis
        #compare x
        #move towards player on x axis
