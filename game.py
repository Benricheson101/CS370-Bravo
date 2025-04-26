from typing import TYPE_CHECKING
import pygame
from os import environ
from Sound import SoundEffects
from pygame.color import Color
from renderer.spritesheet import dos_sprites
from constants import (
    BLINK_EVENT,
    FLASH_EVENT,
    LIGHTGRAY,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    SCALE,
    recalculate_dimensions
)

from level.level_load import set_game_instance
from screens.difficulty import DifficultyScreen
from screens.game import GameScreen
from screens.instructions import InstructionsPage1, InstructionsPage2
from screens.main_menu import MainMenuScreen
from screens.marketing import MarketingScreen
from screens.original_kroz_trilogy import OriginalKrozTrilogyScreen
from screens.screen import ColorMenu
from screens.shareware import SharewareScreen
from screens.story import StoryScreen
from util.color import new_gem_color
from util.state import StateMachine

import sys
import os

if TYPE_CHECKING:
    from entities.player import Player

class Game:

    gem_color: Color
    art_color: Color
    difficulty: int
    sm: StateMachine
    color: bool # color or mono
    fastpc: bool
    player: "Player"

    def __init__(self):
        _, errors = pygame.init()
        if errors:
            print("Error:", errors)
            return

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Kroz")
        self.screen.fill(LIGHTGRAY)
        pygame.time.set_timer(BLINK_EVENT, 333)
        pygame.time.set_timer(FLASH_EVENT, 1_000 // 30)
        
        # Load DOS sprite image ahead of time
        dos_sprites()

        self.sound_effects = SoundEffects()
        self.running = True
        self.clock = pygame.time.Clock()

        # Score/Item tracking
        self.score = 0
        self.key_count = 0
        self.gem_count = 0
        self.whip_count = 0
        self.teleport_count = 0 # needs to be fixed
        self.whip_power = 2 # Initial power

        self.gem_color, self.art_color = new_gem_color()

        self.difficulty = 8
        self.current_level = 13
        self.color = True
        self.fastpc = True

        set_game_instance(self)

        self.sm = StateMachine(self)
        self.sm.add_state("main_menu", MainMenuScreen(self.sm))
        self.sm.add_state("difficulty", DifficultyScreen(self.sm))
        self.sm.add_state("game", GameScreen(self.sm))
        self.sm.add_state("instructions_1", InstructionsPage1(self.sm))
        self.sm.add_state("instructions_2", InstructionsPage2(self.sm))
        self.sm.add_state("marketing", MarketingScreen(self.sm))
        self.sm.add_state("story", StoryScreen(self.sm))
        self.sm.add_state("original_kroz_trilogy", OriginalKrozTrilogyScreen(self.sm))
        self.sm.add_state("color_menu", ColorMenu(self.sm))
        self.sm.add_state("shareware", SharewareScreen(self.sm))
        # set initial scene. since the menus are really slow and annoying to get through, set env KROZ_SKIP_MENUS=1 to skip straight to the game
        self.sm.transition("game" if environ.get("KROZ_SKIP_MENUS") else "color_menu")

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_EQUALS:
                        self.change_scale(0.5)
                        continue
                    elif event.key == pygame.K_MINUS:
                        self.change_scale(-0.5)
                        continue
                    else:
                        self.sm.handle_event(event)
                else:
                    self.sm.handle_event(event)

            self.sm.update()
            self.sm.render(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def change_scale(self, delta: int):
        from constants import SCALE, recalculate_dimensions

        new_scale = SCALE + delta
        if 1.0 <= new_scale <= 5.0:
            # Update SCALE and recalculate
            import constants
            constants.SCALE = new_scale
            constants.recalculate_dimensions()

            pygame.quit()
            # Restart the process with updated SCALE
            os.execv(sys.executable, ['python'] + sys.argv + [str(constants.SCALE)])

    def play_sound(self, sound_type):
        if sound_type == "footstep":
            self.sound_effects.play_sound_in_thread(lambda: self.sound_effects.foot_step(self.fastpc))
        elif sound_type == "grab":
            self.sound_effects.play_sound_in_thread(self.sound_effects.grab_sound)
        elif sound_type == "block":
            self.sound_effects.play_sound_in_thread(self.sound_effects.block_sound)
        elif sound_type == "none":
            self.sound_effects.play_sound_in_thread(self.sound_effects.none_sound)
