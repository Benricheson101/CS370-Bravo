import pygame

from constants import BLINK_EVENT, FLASH_EVENT, LIGHTGRAY, WINDOW_HEIGHT, WINDOW_WIDTH
from game import Game
from renderer.spritesheet import dos_sprites
from screens.difficulty import DifficultyScreen
from screens.instructions import InstructionsPage1, InstructionsPage2
from screens.main_menu import MainMenuScreen
from screens.marketing import MarketingScreen
from screens.original_kroz_trilogy import OriginalKrozTrilogyScreen
from screens.story import StoryScreen
from util.state import StateMachine


# BLINK_EVENT = pygame.event.custom_type()
# FLASH_EVENT = pygame.event.custom_type()

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(LIGHTGRAY)

    game = Game()
    pygame.display.set_caption("Return to Kroz")

    pygame.time.set_timer(BLINK_EVENT, 333)

    # roughly 30/s. unclear how often the original game does it so just picking a random number that looks good
    pygame.time.set_timer(FLASH_EVENT, 33)

    dos_sprites()

    clock = pygame.time.Clock()
    run = True

    game = Game()

    sm = StateMachine(game)

    sm.add_state("main_menu", MainMenuScreen(sm))
    sm.add_state("difficulty", DifficultyScreen(sm))
    sm.add_state("instructions_1", InstructionsPage1(sm))
    sm.add_state("instructions_2", InstructionsPage2(sm))
    sm.add_state("marketing", MarketingScreen(sm))
    sm.add_state("story", StoryScreen(sm))
    sm.add_state("original_kroz_trilogy", OriginalKrozTrilogyScreen(sm))

    sm.transition("main_menu")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                sm.handle_event(event)

        sm.update()
        sm.render(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
