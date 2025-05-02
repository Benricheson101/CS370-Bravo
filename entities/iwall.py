from entities.wall import Wall
from renderer.cell import Cell
from entities.player import Player
from Sound import SoundEffects

class IWall(Wall):
    def __init__(self, color: int = 6) -> None:
        super().__init__(color)
        self.image.fill((0, 0, 0, 0))   # for some reason dos_character(0) didn't work here
        self.is_invisible = True  # Track invisibility state
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: Cell) -> bool:
        if isinstance(cell, Player) and self.is_invisible:
            self.sound_effects.BlockSound(FastPC=True)
            self.load_dos_char(219)  # Reveal wall on collision
            self.is_invisible = False
            from level.level_load import game_instance
            if not Wall.has_paused_message:
                game_instance.sm.current_state.pause_flash(20,25,'A Solid Wall blocks your way.')
                Wall.has_paused_message = True
            if game_instance:
                if game_instance.score > 20:
                    game_instance.score -= 20
        return False
