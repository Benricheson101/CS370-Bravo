from abc import abstractmethod
from pygame import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface


class UIElement(Sprite):
    @property
    @abstractmethod
    def rect(self) -> Rect: pass

    @property
    @abstractmethod
    def image(self) -> Surface: pass

    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, self.rect)

    def update(self) -> None:
        pass
