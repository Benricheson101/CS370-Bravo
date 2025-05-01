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

        self.last_move_time = current_time

        from gameState import is_frozen
        if is_frozen():
            return

        player_pos = pygame.Vector2(player.x, player.y)
        my_pos = pygame.Vector2(self.x, self.y)
        direction = player_pos - my_pos

        # Don't move if this move would place us on top of the player
        direction_length = direction.length()
        if direction_length == 0:
            return  # Already on the player (should never happen)

        # Calculate next tile if we move in this direction
        move_vector = direction.normalize() * self.speed
        target_x = round(self.x + move_vector.x)
        target_y = round(self.y + move_vector.y)

        # Cancel move if that tile *is* the player
        if (target_x, target_y) == (player.x, player.y):
            return

        self.move(move_vector)

    def on_collision(self, cell):
        from level.level_load import game_instance

        if isinstance(cell, Player):
            if not MBlock.has_paused_message:
                game_instance.sm.current_state.pause_flash(19,25,'A Moving Wall blocks your way.')
                MBlock.has_paused_message = True
            if game_instance.score > 20:
                game_instance.score -= 20
                
            

        self.sound_effects.play_in_thread(self.sound_effects.BlockSound, True)

        # Whip and enemy logic (destroy self)
        if hasattr(cell, "is_enemy") or hasattr(cell, "is_whip"):
            if self.grid:
                self.grid.remove((self.x, self.y))
            return True

        return False
