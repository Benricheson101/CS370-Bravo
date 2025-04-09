from pygame import Surface
import pygame
from pygame.event import Event
from constants import BLACK, BLUE, GAME_GRID_COLS, GAME_GRID_ROWS, GAME_GRID_WIDTH, GRID_CELL_WIDTH, SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS
# from level.level_load import restore_level, save_level
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

def load_current_level(self):
        # Check for even-numbered levels (randomly generated)
        if self.game.current_level % 2 == 0:
            from level.level_load import random_level, object_counts
            random_level(self.game_grid, self.game.current_level, object_counts)
        else:
            from level.level_load import load_level
            load_level(self.grid, self.game.current_level)

class GameScreen(State):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)
        
        self.game = sm.game

        self.scoreboard = CellGrid(
            grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
            offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
            fill=BLUE,
            game=sm.game,
        )

        self.grid = CellGrid(
            grid_size=(GAME_GRID_COLS+2, GAME_GRID_ROWS+2),
            # offset=(GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
            fill=BLACK,
            game=sm.game,
        )
        self.grid.border()

        self.game_grid = self.grid # cus some other stuff uses game_grid

        # load_level(self.game_grid, 1)
        self.current_level = 1
        
        load_current_level(self)

    def update(self, **kwargs):
        self.grid.update(**kwargs)
        self.scoreboard.update(**kwargs)

    def render(self, screen: Surface):
        self.grid.render(screen)
        self.scoreboard.render(screen)

    # def handle_event(self, event: Event):
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_s:
    #             save_level(self.grid)
    #         elif event.key == pygame.K_r:
    #             restore_level(self.grid)
                
    
