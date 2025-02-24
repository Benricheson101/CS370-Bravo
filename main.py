import pygame
from constants import (
    BLACK,
    BLUE,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GAME_GRID_WIDTH,
    GRAY,
    GRID_CELL_HEIGHT,
    GRID_CELL_WIDTH,
    ORANGE,
    SCOREBOARD_GRID_COLS,
    SCOREBOARD_GRID_ROWS,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)
from entities.player import Player
from renderer.cell import Cell
from renderer.cell_grid import CellGrid


class WallTile(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(ORANGE)

def main():
    _, errors = pygame.init()
    if errors:
        print("Error:", errors)
        return

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Kroz")
    screen.fill(GRAY)

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

    game.put((0, 0), player)
    game.put((1, 0), WallTile())
    game.put((0, 1), WallTile())

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
