from pygame.event import Event
from ui.game import Game
from ui.state import GameState, StateMachine
from ui.text import Text

import pygame
from pygame.surface import Surface


RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

class TitleScene(GameState):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        txt = Text("TITLE SCENE", fg=WHITE, bg=BLUE, center=(400, 200))

        game_button = Text("Start Game", fg=WHITE, bg=BLUE, center=(400, 500))
        # TODO: make this more ergonomic to use (pass event to UIElement?)
        self.game_button = game_button

        self.sprites = pygame.sprite.Group()

        self.sprites.add(txt)
        self.sprites.add(game_button)

    def draw(self, surface: Surface):
        surface.fill(BLACK)
        self.sprites.draw(surface)

    def on_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.game_button.rect.collidepoint(event.pos):
                self.sm.next_state = GameScene(self.sm)

class GameScene(GameState):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        txt = Text("GAME SCENE", fg=WHITE, bg=RED, center=(400, 200))

        title_button = Text("Back to Title", fg=WHITE, bg=RED, center=(400, 500))
        # TODO: make this more ergonomic to use (pass event to UIElement?)
        self.title_button = title_button

        self.sprites = pygame.sprite.Group()

        self.sprites.add(txt)
        self.sprites.add(title_button)

    def draw(self, surface: Surface):
        surface.fill(BLACK)
        self.sprites.draw(surface)

    def on_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.title_button.rect.collidepoint(event.pos):
                self.sm.next_state = TitleScene(self.sm)

def main():
    WIDTH = 800
    HEIGHT = 600

    sm = StateMachine()

    pygame.init()
    game = Game(sm, WIDTH, HEIGHT)

    title_scene = TitleScene(sm)
    # game_scene = GameScene()

    game.run(title_scene)

if __name__ == "__main__":
    main()
