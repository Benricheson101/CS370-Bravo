import pygame
from renderer.spritesheet import dos_sprites
from constants import (
    BLACK,
    BLUE,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GAME_GRID_WIDTH,
    GRAY,
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
# from level_load import (
#     game,
#     load_level
# )

# test
from level_data import level_data

tile_mapping = {
    "P": Player(),
    "#": Wall(),
    "X": Block(),
    "1": Enemy(),
    "+": Gem(),
    "T": Teleport(),
    " ": None
    }


    



def main():
    _, errors = pygame.init()
    if errors:
        print("Error:", errors)
        return

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Kroz")
    screen.fill(GRAY)

    # load dos sprite image ahead of time so it doesn't slow the running game
    dos_sprites()

    

    scoreboard = CellGrid(
        grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
        offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
        fill=BLUE
    )
    
    game = CellGrid(
        grid_size=(GAME_GRID_COLS, GAME_GRID_ROWS),
        offset=(GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
        fill=BLACK
    )
    def load_level(level_num):
        entity_positions = []
        for i, row in enumerate(level_data[f"level_{level_num}"]):
            for j, value in enumerate(row):
                if value in tile_mapping:
                    entity_positions.append(game.put((j, i), tile_mapping.get(value, None)))
        for i in range(len(entity_positions)):
            return entity_positions[i]

    player = Player()

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
