import pygame
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
    game,
    load_level,
    save_level,
    restore_level,
    set_game_instance
)

class Game:
    def __init__(self):
        _, errors = pygame.init()
        if errors:
            print("Error:", errors)
            return

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Kroz")
        self.screen.fill(LIGHTGRAY)

        # Load DOS sprite image ahead of time
        dos_sprites()

        # Initialize scoreboard
        self.scoreboard = CellGrid(
            grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
            offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
            fill=BLUE
        )

        # Load initial level
        load_level(9)

        # Game loop control
        self.running = True
        self.clock = pygame.time.Clock()

        # Score tracking
        self.score = 0
        
        # Key count tracking
        self.key_count = 0
        
        # Register the Game instance globally in level_load.py
        set_game_instance(self) 

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        save_level()
                    elif event.key == pygame.K_r:
                        restore_level()

            if not self.running:
                break  # Ensure we exit before rendering again

            game.render(self.screen)
            self.scoreboard.render(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit() 

    

