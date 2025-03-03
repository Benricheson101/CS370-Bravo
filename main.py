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
from level_load import (
    game,
    load_level
)


def main():
    _, errors = pygame.init()
    if errors:
        print("Error:", errors)
        return

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Kroz")
    screen.fill(LIGHTGRAY)

    # load dos sprite image ahead of time so it doesn't slow the running game
    dos_sprites()

    

    scoreboard = CellGrid(
        grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
        offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
        fill=BLUE
    )
    
    
    load_level(1)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.render(screen)
        scoreboard.render(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
