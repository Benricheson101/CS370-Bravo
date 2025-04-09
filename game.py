import pygame
from os import environ
from pygame.color import Color
from entities.char import Char
from renderer.spritesheet import dos_sprites
from constants import (
    BLACK,
    BLINK_EVENT,
    BLUE,
    FLASH_EVENT,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GAME_GRID_WIDTH,
    LIGHTGRAY,
    GRID_CELL_WIDTH,
    SCOREBOARD_GRID_COLS,
    SCOREBOARD_GRID_ROWS,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

from renderer.cell_grid import CellGrid
from level.level_load import (
    load_level,
    save_level,
    restore_level,
    set_game_instance,
)
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

# level switch import


class Game:
 
    gem_color: Color
    art_color: Color


    difficulty: int

    sm: StateMachine
    color: bool # color or mono
    fastpc: bool

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

        # Game loop control
        self.running = True
        self.clock = pygame.time.Clock()

        # Score tracking
        self.score = 0

        # Key count tracking
        self.key_count = 0

        #Gem count tracking
        self.gem_count = 0

        #Whip count Tracking
        self.whip_count = 0

        #Teleport count Tracking
        self.teleport_count = 0

        self.gem_color, self.art_color = new_gem_color()

        self.difficulty = 8

        # Register the Game instance globally in level_load.py
        set_game_instance(self)
        
        # level
        self.current_level = 1

        self.color = True
        self.fastpc = True

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
                else:
                    self.sm.handle_event(event)

            self.sm.update()
            self.sm.render(self.screen)

            print(f"Score: {self.score}, Keys: {self.key_count}, Gems: {self.gem_count}, "
                  f"Whips: {self.whip_count}, Teleports: {self.teleport_count}")

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

        ''' def handle_input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                # Make sure self.player exists
                if hasattr(self, 'player'):
                    self.player.use_whip()'''



