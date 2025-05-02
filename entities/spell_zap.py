'''
OBJECT:  Creature zap spell
APPEARANCE:  Red filled arrow
METADATA:  %
POINT VALUE:  formula based on number of enemies killed (150 max)

This handy spell decimates the enemies on the level, selecting them randomly.
As many as 40 enemies are killed with a single spell.

'''

import random
from constants import YELLOW
from entities.player import Player
from renderer.cell import Cell
from entities.enemy import Enemy
from entities.enemy_medium import Enemy_Medium
from entities.enemy_hard import Enemy_Hard
from Sound import SoundEffects

class Spell_Zap(Cell):
    has_paused_message = False
    def __init__(self) -> None:
        super().__init__()
        self.col(12,7)
        self.load_dos_char(30)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            self.sound_effects.grabsoudn()
            from level.level_load import game_instance
            if not Spell_Zap.has_paused_message:
                game_instance.sm.current_state.pause_flash(25,25,'A Creature Zap Spell!')
                Spell_Zap.has_paused_message = True

            for y in range(self.grid.rows):
                for x in range(self.grid.cols):
                    pos = (x, y)
                    if self.grid.at(pos):
                        target = self.grid.at(pos)
                        if isinstance(target, Enemy) and random.random() < 0.5: #50% chance
                            self.grid.remove(pos)
                        elif isinstance(target, Enemy_Medium) and random.random() < 0.3:
                            self.grid.remove(pos)
                        elif isinstance(target, Enemy_Hard) and random.random() < 0.2:
                            self.grid.remove(pos)


            return True

        return False
