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
        d = pygame.math.Vector2()

        if keys[pygame.K_LEFT] ^ keys[pygame.K_RIGHT]:
            d.x = 1 if keys[pygame.K_RIGHT] else -1

        if keys[pygame.K_UP] ^ keys[pygame.K_DOWN]:
            d.y = 1 if keys[pygame.K_DOWN] else -1

        if d.length() > 0:
            d.normalize_ip()
            # FIXME: add a movement delay
            self.move(d)
            # TODO: sound here
