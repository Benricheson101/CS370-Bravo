from renderer.cell import Cell
from entities.player import Player


class Wall(Cell):
    def __init__(self, color: int = 6) -> None:
        super().__init__()
        self.col(color, 7)
        self.bak(color, 7)
        self.load_dos_char(219)

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player):
            print('A Solid Wall blocks your way.')
            from level.level_load import game_instance
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        return False



