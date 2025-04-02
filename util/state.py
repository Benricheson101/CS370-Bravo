# class StateMachine:
#     def __init__(self) -> None:
#         self.current_state = None
#         self.next_state = None
#
#     def transition(self, state):
#         self.next_state = state
#
#     def update(self) -> None:
#         if self.next_state is not None:
#             self.current_state = self.next_state
#             self.next_state = None
#
# # class GameStateWrapper:
# #     def __init__(self):
# #         self.done = False
# #         self.next = None
#
# class GameState:
#     sm: StateMachine
#
#     def __init__(self, sm: StateMachine) -> None:
#         self.sm = sm

from typing import Optional

from pygame.event import Event

from constants import BLACK, BLINK_EVENT, FLASH_EVENT, SCREEN_GRID_COLS, SCREEN_GRID_ROWS, SCREEN_SIZE
from game import Game
from renderer.cell_grid import CellGrid

class State:
    sm: "StateMachine"
    grid: CellGrid

    def __init__(self, sm: "StateMachine") -> None:
        self.sm = sm
        self.grid = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLACK,
            game=sm.game,
        )

    def enter(self): pass
    def exit(self): pass

    def _handle_event(self, event: Event):
        if event.type == FLASH_EVENT:
            self.grid._flip_flash()
        elif event.type == BLINK_EVENT:
            self.grid._flip_blink()

        self.handle_event(event)

    def handle_event(self, event: Event): pass

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def render(self, screen):
        self.grid.render(screen)

class StateMachine:
    current_state: Optional[State]
    game: Game

    states: dict[str, State]

    def __init__(self, game: Game) -> None:
        self.current_state = None
        self.game = game
        self.states = {}

    def add_state(self, name: str, state: State):
        self.states[name] = state

    def transition(self, state: str):
        assert self.states[state] is not None, f"cannot transition to state {state}, state does not exist"
        self.transition_to(self.states[state])

    def transition_to(self, new_state: State):
        if self.current_state is not None:
            self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def handle_event(self, event):
        assert self.current_state, "Cannot handle event when no state is present"
        self.current_state._handle_event(event)

    def update(self, **kwargs):
        if self.current_state is None:
            return

        self.current_state.update(**kwargs)

    def render(self, screen):
        if self.current_state is None:
            print("tried to render but no current state")
            return

        self.current_state.render(screen)

# class StartupMenuState(State):
#     def __init__(self, sm: StateMachine) -> None:
#         super().__init__(sm)
