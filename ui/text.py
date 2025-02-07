from typing import Optional

import pygame.freetype
from pygame import Rect
from pygame.surface import Surface

from .element import UIElement

class Text(UIElement):
    def __init__(self, text: str, fg: tuple[int, int, int], bg: Optional[tuple[int, int, int]]=None, font_size=20, font_name="Courier New", **kwargs) -> None:

        super().__init__()

        font = pygame.freetype.SysFont(font_name, font_size)
        surface, _ = font.render(text, bgcolor=bg, fgcolor=fg)

        self.text_image = surface.convert_alpha()
        self.text_rect = self.text_image.get_rect(**kwargs)

    @property
    def image(self) -> Surface:
        return self.text_image

    @property
    def rect(self) -> Rect:
        return self.text_rect
