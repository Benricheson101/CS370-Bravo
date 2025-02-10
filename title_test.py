# based on: https://programmingpixels.com/handling-a-title-screen-game-flow-and-buttons-in-pygame.html

import pygame
from pygame.constants import MOUSEBUTTONUP
import pygame.freetype
from pygame.sprite import Sprite

from state import GameState

BLUE = (0, 0, 255)
SKYBLUE = (66, 135, 245)
WHITE = (255, 255, 255)

def create_surface_with_text(text: str, font_size: int, text_rgb: tuple[int, int, int], bg_rgb: tuple[int, int, int]):
    font = pygame.freetype.SysFont("Courier New", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, hover_rgb, action=None):
        self.mouse_over = False

        # default text
        default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)

        # hover text
        highlighted_image = create_surface_with_text(
            text,
            font_size,
            hover_rgb,
            bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
                default_image.get_rect(center=center_position),
                highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos: tuple[int, int], mouse_up: bool):
        self.mouse_over = self.rect.collidepoint(mouse_pos)
        if self.mouse_over and mouse_up:
            return self.action

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def title_scene(screen: pygame.Surface) -> GameState:
    ui_elements = []

    lines = [
        "kroz game blah blah",
        "rules here probably",
        "i forget how this looks in the game",
    ]

    start = (400, 200)
    spaced = 30

    for i, line in enumerate(lines):
        elem = UIElement(
            center_position=(start[0], start[1] + spaced * i),
            font_size=30,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            hover_rgb=SKYBLUE,
            text=line
        )

        ui_elements.append(elem)

    start_button = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=SKYBLUE,
        text_rgb=WHITE,
        hover_rgb=WHITE,
        text="start",
        action=GameState.GAME,
    )

    ui_elements.append(start_button)

    while True:
        mouse_up = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        screen.fill(BLUE)

        for elem in ui_elements:
            action = elem.update(pygame.mouse.get_pos(), mouse_up)
            if action is not None:
                return action

            elem.draw(screen)

        pygame.display.flip()

def game_scene(screen: pygame.Surface) -> GameState:
    text = UIElement(
        center_position=(400, 200),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        hover_rgb=WHITE,
        text="game goes here",
    )

    title_button = UIElement(
        center_position=(400, 370),
        font_size=30,
        bg_rgb=SKYBLUE,
        text_rgb=WHITE,
        hover_rgb=WHITE,
        text="back to title",
        action=GameState.TITLE,
    )

    quit_button = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=SKYBLUE,
        text_rgb=WHITE,
        hover_rgb=WHITE,
        text="quit",
        action=GameState.QUIT,
    )

    ui_elements = [text, title_button, quit_button]

    while True:
        mouse_up = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        screen.fill(BLUE)

        for elem in ui_elements:
            action = elem.update(pygame.mouse.get_pos(), mouse_up)
            if action is not None:
                return action

            elem.draw(screen)

        pygame.display.flip()

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    game_state: GameState = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_scene(screen)

        elif game_state == GameState.GAME:
            game_state = game_scene(screen)

        elif game_state == GameState.QUIT:
            print("quitting")
            pygame.quit()
            return

        else:
            raise Exception(f"Unhandled game state: {game_state}")

if __name__ == "__main__":
    main()
