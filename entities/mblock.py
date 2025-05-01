from entities.enemy import Enemy
from entities.player import Player
from Sound import SoundEffects
import pygame

class MBlock(Enemy):
    sound_effects = SoundEffects()
    has_paused_message = False

    def __init__(self) -> None:
        super().__init__()
        self.col(6, 7)
        self.load_dos_char(178)

    def is_breakable_wall(self): 
        return True

    def update(self, **kwargs):
        if not self.grid:
            return

        player = self.grid.game.player
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time < self.move_time:
            return

        from gameState import is_frozen
        if is_frozen():
            return

        self.last_move_time = current_time

        dx = player.x - self.x
        dy = player.y - self.y

        # Clamp movement to at most 1 step
        dx = max(-1, min(1, dx))
        dy = max(-1, min(1, dy))

        target_pos = (self.x + dx, self.y + dy)

        # Don't move into the player
        if target_pos == (player.x, player.y):
            return

        # Don't move if outside grid
        if not (0 <= target_pos[0] < self.grid.cols and 0 <= target_pos[1] < self.grid.rows):
            return

        target_cell = self.grid.at(target_pos)
        if isinstance(target_cell, MBlock):  # Don't walk into other MBlocks
            return

        self.grid.move_to(target_pos, self)


    def on_collision(self, cell):
        from level.level_load import game_instance

        if isinstance(cell, Player):
            if not MBlock.has_paused_message:
                game_instance.sm.current_state.pause_flash(19,25,'A Moving Wall blocks your way.')
                MBlock.has_paused_message = True
            if game_instance.score > 20:
                game_instance.score -= 20
        if isinstance(cell, Enemy): # Enemy dies when it moves into Block
            if cell.grid:
                cell.grid.remove((cell.x, cell.y))  # Remove Enemy
            if self.grid:
                self.grid.remove((self.x, self.y))  # Remove Block
            return False
        return False
                
            

        self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)

        # Whip and enemy logic (destroy self)
        if hasattr(cell, "is_enemy") or hasattr(cell, "is_whip"):
            if self.grid:
                self.grid.remove((self.x, self.y))
            return True

        return False
