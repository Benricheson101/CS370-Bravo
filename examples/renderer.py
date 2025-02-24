import pygame
from pygame.color import Color
from constants import (
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GAME_GRID_WIDTH,
    GRID_CELL_HEIGHT,
    GRID_CELL_WIDTH,
    SCOREBOARD_GRID_COLS,
    SCOREBOARD_GRID_ROWS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)
from renderer.cell_grid import Cell, CellGrid


RED = Color(0xFF0000FF)
GREEN = Color(0x00FF00FF)
BLUE = Color(0x0000FFFF)
GRAY = Color(0x808080FF)
BLACK = Color(0x000000FF)

class TestCell(Cell):
    def __init__(self, fill: Color) -> None:
        super().__init__()
        self.image.fill(fill)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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

    game.put((0, 0), TestCell(RED))
    game.put((1, 1), TestCell(GREEN))
    game.put((2, 2), TestCell(BLUE))

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
