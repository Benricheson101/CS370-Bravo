from typing import Optional
import pygame
from pygame.rect import Rect
from pygame.surface import Surface

class SpriteSheet:
    def __init__(self, filename, sprite_size: tuple[int, int]) -> None:
        self.sprite_size = sprite_size
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as message:
            print("Unable to load spritesheet:", message)
            raise SystemExit(message)

    def image_at(self, rectangle: Rect):
        rect = Rect(rectangle)
        image = Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        return image

    def images_at(self, rects: list[Rect]) -> list[Surface]:
        return [self.image_at(rect) for rect in rects]

    # def load_strip(self, rect: Rect, count: int) -> list[Surface]:
    #     rects = [Rect(rect[0] + rect[2] * x, rect[1], rect[2], rect[3]) for x in range(count)]
    #     return self.images_at(rects)

    def sprite(self, pos: tuple[int, int]):
        x, y = pos
        w, h = self.sprite_size

        rect = Rect((x * w, y * h, w, h))
        return self.image_at(rect)

dos_font: Optional[SpriteSheet] = None

def dos_sprites():
    global dos_font

    if dos_font is None:
        print("initializing dos_font")
        dos_font = SpriteSheet("./assets/spritesheet.png", (9, 16))

    return dos_font
