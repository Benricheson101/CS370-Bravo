import pygame

from constants import BLACK, LIGHTGRAY, SCREEN_GRID_COLS, SCREEN_GRID_ROWS, WINDOW_HEIGHT, WINDOW_WIDTH
from renderer.cell_grid import CellGrid
from screens.screen import color_menu
from screens.title import instructions2, main_menu, marketing, original_kroz_trilogy, instructions1, story

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(LIGHTGRAY)

    g = CellGrid(
        grid_size=(SCREEN_GRID_COLS, SCREEN_GRID_ROWS),
        fill=BLACK
    )

    # original_kroz_trilogy(g)
    tick_fn = main_menu(g)
    # color_menu(g)
    # instructions1(g)
    # instructions2(g)
    # marketing(g)
    # tick_fn = story(g)

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if callable(tick_fn):
            tick_fn()

        g.update()
        g.render(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
