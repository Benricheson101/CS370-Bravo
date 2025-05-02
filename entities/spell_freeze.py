'''
OBJECT:  Freeze time spell
APPEARANCE:  Light blue f
METADATA:  Z
POINT VALUE:  20 or 10

When picked up, enemies will stop their movement rate for a brief period.
'''

from constants import LIGHTBLUE
from entities.player import Player
from renderer.cell import Cell
from gameState import freeze_enemies_for
from Sound import SoundEffects


class Spell_Freeze(Cell):
    has_paused_message = False
    def __init__(self):
        super().__init__()
        self.load_dos_char(102, LIGHTBLUE)
        
    sound_effects = SoundEffects()

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.GrabSound()
            freeze_enemies_for(8000)
            from level.level_load import game_instance
            if not Spell_Freeze.has_paused_message:
                game_instance.sm.current_state.pause_flash(13,25,'You have activated a Freeze Creature spell!')
                Spell_Freeze.has_paused_message = True
            return True
        
        return False

    def update(self, **kwargs):
        return super().update(**kwargs)
