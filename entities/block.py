from renderer.cell import Cell
from entities.player import Player


class Block(Cell):
    """
    A crumbled wall. For some reason the pascal code calls it "Block"
    """
    def __init__(self) -> None:
        super().__init__()
        self.col(6,7)
        self.load_dos_char(178)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print('A Crumbled Wall blocks your way.')
            from level.level_load import game_instance
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        return False
