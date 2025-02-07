from typing import Optional
import pygame

from .state import GameState, StateMachine


# from: https://www.reddit.com/r/pygame/comments/16zzfr5

class Game:
    def __init__(self, sm: StateMachine, width: int, height: int) -> None:
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        self.sm = sm

    def game_loop(self):
        while self.running:
            self.sm.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    if self.sm.current_state is not None:
                        self.sm.current_state.on_event(event)

            if self.sm.current_state is not None:
                self.sm.current_state.update()
                self.sm.current_state.draw(self.screen)

            pygame.display.flip()

    def run(self, starting_state) -> None:
        self.sm.current_state = starting_state
        self.game_loop()
