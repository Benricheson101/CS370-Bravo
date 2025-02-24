import pygame
from constants import YELLOW
from renderer.cell import Cell


class Player(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(YELLOW)

    def update(self) -> None:
        assert self.grid

        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] ^ keys[pygame.K_RIGHT]:
            dx = 1 if keys[pygame.K_RIGHT] else -1

        if keys[pygame.K_UP] ^ keys[pygame.K_DOWN]:
            dy = 1 if keys[pygame.K_DOWN] else -1

        if dx or dy:
            # FIXME: add a movement delay
            self.move((dx, dy))
            # TODO: sound here
