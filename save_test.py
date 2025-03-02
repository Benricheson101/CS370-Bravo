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
from entities.block import Block
from entities.gem import Gem
from entities.player import Player
from entities.wall import Wall
from renderer.cell_grid import CellGrid
from entities.teleport import Teleport
from entities.enemy import Enemy
from level_load import (
    game,
    load_level,
    save_level,
    restore_level
)
# test
from level_data import level_data


scoreboard = CellGrid(
        grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
        offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
        fill=BLUE
    )



            

LEVEL_1 = 1



# idk if this is needed or not
pygame.init()

def level_1(screen):
    _, errors = pygame.init()
    if errors:
        print("Error:", errors)
        return

    
    pygame.display.set_caption("Level 1")
    screen.fill(LIGHTGRAY)

    # load dos sprite image ahead of time so it doesn't slow the running game
    dos_sprites()

    load_level(1)
    
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:    # Go to Level 2
                    save_level()
                    
                elif event.key == pygame.K_r:    # Go to Level 3
                    restore_level()
                    
        game.render(screen)
        scoreboard.render(screen)
        pygame.display.flip()
        clock.tick(60)
    

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    scene = LEVEL_1
    while True:
        if scene == LEVEL_1:
            scene = level_1(screen)
        
    
main()
