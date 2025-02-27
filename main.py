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
from level_data import (
    wall_pos,
    gem_pos,
    player_pos,
    enemy_pos
)


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

    game = CellGrid(
        grid_size=(GAME_GRID_COLS, GAME_GRID_ROWS),
        offset=(GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
        fill=BLACK
    )

    scoreboard = CellGrid(
        grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
        offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
        fill=BLUE
    )

    player = Player()

    # game.put((0, 0), player)
    # game.put((4, 0), Wall())
    # game.put((0, 1), Wall())
    # game.put((5, 5), Gem())
    # game.put((10,10), Teleport())
    # game.put((20,20), Enemy())
    game.put((player_pos[0][0], player_pos[0][1]), player)
    # game.put((4, 0), Wall())
    # game.put((0, 1), Wall())
    # game.put((2, 0), Gem())
    # from level_data.py: import positions of walls
    for i in range (len(wall_pos)):
        game.put((wall_pos[i][0], wall_pos[i][1]), Wall())
    for i in range(len(gem_pos)):
        game.put((gem_pos[i][0], gem_pos[i][1]), Gem())
    for i in range(len(enemy_pos)):
        game.put((enemy_pos[i][0], enemy_pos[i][1]), Enemy())

    game.put((player_pos[0][0]+1, player_pos[0][1]), Teleport())
    game.put((player_pos[0][0]+2, player_pos[0][1]), Gem())
    game.put((player_pos[0][0]+3, player_pos[0][1]), Wall())
    game.put((player_pos[0][0]+4, player_pos[0][1]), Block())

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
