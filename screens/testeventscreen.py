import pygame
from pygame.event import Event
from constants import BLACK, SCREEN_SIZE
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine


class TestEventScreen(State):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        self.grid = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLACK,
            game=sm.game,
        )

        self.grid.gotoxy(10, 10)
        self.grid.write("Key pressed: ")

        self.startsat = self.grid.cur_pos

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        event_name = pygame.event.event_name(event.type)
        x, y = self.grid.cur_pos

        if event_name == "UserEvent":
            return

        for i in range(len(self.grid.grid[2])):
            self.grid.remove((i, 2))

        self.grid.gotoxy(2, 3)
        self.grid.write(event_name)
        self.grid.gotoxy(x+1,y+1)

            # if self.grid.cur_pos[0] > 40:
            #     y+=1
            #     # self.grid.gotoxy(self.startsat[0]+1, y + 2)
            #
            # xpos = self.startsat[0] + 1 if x >= 40 else self.grid.cur_pos[0] + 2
            # ypos = y + 2 if x >= 40 else y+1
            # self.grid.gotoxy(xpos,ypos)
            # self.grid.flash(xpos, ypos, chr(event.key))

        if event.type == pygame.KEYDOWN:
            if self.grid.cur_pos[0] > 40:
                self.grid.gotoxy(self.startsat[0]+1, y + 2)
            self.grid.write(chr(event.key))
