from pygame import Rect, Surface
from pygame.sprite import Sprite
from constants import GRID_CELL_HEIGHT, GRID_CELL_WIDTH


class Cell(Sprite):
    rect: Rect
    image: Surface

    def __init__(self, width = GRID_CELL_WIDTH, height = GRID_CELL_HEIGHT) -> None:
        super().__init__()

        self.image = Surface((width, height))
        self.rect = self.image.get_rect()

    def render(self, parent: Surface):
        parent.blit(self.image, self.rect)

