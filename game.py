import pygame
from pygame.color import Color
from renderer.spritesheet import dos_sprites
from constants import (
    BLACK,
    BLUE,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GAME_GRID_WIDTH,
    LIGHTGRAY,
    GRID_CELL_HEIGHT,
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
from util import new_gem_color

FLASH_EVENT = pygame.event.custom_type()

class Game:
    
    def load_current_level(self):
        # Check for even-numbered levels (randomly generated)
        if self.current_level % 2 == 0:
            from level.level_load import random_level, object_counts
            random_level(self.game_grid, self.current_level, object_counts)
        else:
            from level.level_load import load_level
            load_level(self.game_grid, self.current_level)
    
    
    gem_color: Color
    art_color: Color

    game_grid: CellGrid

    def __init__(self):
        _, errors = pygame.init()
        if errors:
            print("Error:", errors)
            return

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Kroz")
        self.screen.fill(LIGHTGRAY)
        pygame.time.set_timer(FLASH_EVENT, 333)

        # Load DOS sprite image ahead of time
        dos_sprites()

        # Initialize scoreboard
        self.scoreboard_grid = CellGrid(
            grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
            offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
            fill=BLUE,
            game=self,
        )

        self.game_grid = CellGrid(
            grid_size=(GAME_GRID_COLS+2, GAME_GRID_ROWS+2),
            # offset=(GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
            fill=BLACK,
            game=self,
        )

        self.game_grid.border()

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

        # Register the Game instance globally in level_load.py
        set_game_instance(self)

        # Load initial level
        self.current_level = 1
        self.load_current_level()
        



    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        save_level(self.game_grid)
                    elif event.key == pygame.K_r:
                        restore_level(self.game_grid)
                elif event.type == FLASH_EVENT:
                    self.game_grid._flip_blink()

            if not self.running:
                break  # Ensure we exit before rendering again

            self.game_grid.update()
            self.game_grid.render(self.screen)
            self.scoreboard_grid.update()
            self.scoreboard_grid.render(self.screen)

            print(f"Score: {self.score}, Keys: {self.key_count}, Gems: {self.gem_count}, "
                  f"Whips: {self.whip_count}, Teleports: {self.teleport_count}")

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()



