from typing import Optional
import pygame
from pygame.event import Event
from pygame.surface import Surface

from .text import Text

BLUE=(0, 0, 255)
WHITE=(255, 255, 255)

class StateMachine:
    def __init__(self) -> None:
        self.current_state: Optional[GameState] = None
        self.next_state: Optional[GameState] = None

    def update(self) -> None:
        if self.next_state is not None:
            self.current_state = self.next_state
            self.next_state = None


# TODO: make this inherit from sprite group?
class GameState:
    def __init__(self, state_machine: StateMachine) -> None:
        # waits until done=True to transition to next state
        self.done = False
        # the next state to be rendered when `self.done=True`
        self.next = None
        self.sm = state_machine

    def on_event(self, event: Event) -> None: pass

    def update(self): pass
    def draw(self, surface: Surface): pass

class TitleScreen(GameState):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        font = pygame.font.SysFont(
            name="Courier New",
            size=20
        )

        self.text = font.render(
            text="kroz",
            antialias=True,
            color=WHITE,
        )

        self.text_rect = self.text.get_rect(topleft=(20, 20))

    def draw(self, surface):
        surface.fill(BLUE)
        surface.blit(self.text, self.text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    test_text = Text("test text", fg=WHITE, bg=BLUE, center=(400, 400))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return


        screen.fill(BLUE)
        test_text.update()
        test_text.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
