from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects 
from entities.enemy import Enemy


class Block(Cell):
    """
    A crumbled wall. For some reason the pascal code calls it "Block"
    """
    has_paused_message = False
    sound_effects = SoundEffects()  # Initialize the sound effects
    def __init__(self) -> None:
        super().__init__()
        self.col(6,7)
        self.load_dos_char(178)
        #SOUND
        self.fast_pc = False
        
    def is_breakable_wall(self): return True

    def on_collision(self, cell: "Cell") -> bool:
        
        if isinstance(cell, Player):
            from level.level_load import game_instance

            if not Block.has_paused_message:
                sm = game_instance.sm
                sm.current_state.pause(True)
                self.grid.flash(18, 25, 'A Crumbled Wall blocks your way.')
                sm.current_state.pause_reason = "block"
                Block.has_paused_message = True
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)
        
        if isinstance(cell, Enemy): # Enemy dies when it moves into Block
            print("Enemy and Block destroyed!")
            if cell.grid:
                cell.grid.remove((cell.x, cell.y))  # Remove Enemy
            if self.grid:
                self.grid.remove((self.x, self.y))  # Remove Block
            return False
        return False
