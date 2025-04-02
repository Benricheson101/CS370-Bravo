import pygame
from pygame.event import Event
from constants import BLACK, BLUE, BROWN, COLORS, LIGHTBLUE, LIGHTCYAN, LIGHTGRAY, LIGHTGREEN, LIGHTRED, RED, SCREEN_SIZE, WHITE, YELLOW
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

class MainMenuScreen(State):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        self.grid.fill = BLACK

        # bor(1)
        self.grid.bak(BLACK, BLACK)
        self.grid.clrscr()
        # cur(3)
        self.grid.col(WHITE, LIGHTBLUE)
        self.grid.gotoxy(33,2)
        self.grid.write('RETURN TO KROZ')
        self.grid.gotoxy(17,4)
        self.grid.col(BROWN, LIGHTGRAY)
        self.grid.write('Copyright (c) 1990 Apogee Software Productions')
        self.grid.gotoxy(7,6)
        self.grid.write('Version 1.2 -- Volume I of the Super Kroz Trilogy by Scott Miller')
        self.grid.gotoxy(1,8)
        self.grid.col(RED, LIGHTGRAY)
        # for x := 1 to 80 do write(#196)
        for _ in range(1, 80):
            self.grid.write(chr(196))
        self.grid.col(YELLOW,WHITE)
        self.grid.gotoxy(28,12)
        self.grid.write('B')
        self.grid.col(COLORS[11],COLORS[7])
        self.grid.write('egin your descent into Kroz...')
        self.grid.col(COLORS[14],COLORS[15])
        self.grid.gotoxy(28,14)
        self.grid.write('I')
        self.grid.col(COLORS[11],COLORS[7])
        self.grid.write('nstructions')
        self.grid.col(COLORS[14],COLORS[15])
        self.grid.gotoxy(28,16)
        self.grid.write('M')
        self.grid.col(COLORS[11],COLORS[7])
        self.grid.write('arketing Kroz')
        self.grid.col(COLORS[14],COLORS[15])
        self.grid.gotoxy(28,18)
        self.grid.write('S')
        self.grid.col(COLORS[11],COLORS[7])
        self.grid.write('tory Behind Kroz')
        self.grid.col(COLORS[14],COLORS[15])
        self.grid.gotoxy(28,20)
        self.grid.write('O')
        self.grid.col(COLORS[11],COLORS[7])
        self.grid.write('riginal Kroz Trilogy')
        self.grid.gotoxy(27,23)
        self.grid.col(COLORS[15],COLORS[0]);self.grid.bak(BLUE, LIGHTGRAY)
        self.grid.write('Your choice (B/I/M/S/O)? B'); #self.grid.gotoxy(wherex-1,wherey); what is wherex wherey
        self.grid.cur(2)
        # ClearKeys
        # read(kbd,ch)
        # if upcase(ch)='R' then MixUp:=true else MixUp:=false
        # ClearKeys
        # cur(3)

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            transition_map = {
                pygame.K_b: "game",
                pygame.K_i: "instructions_1",
                pygame.K_m: "marketing",
                pygame.K_s: "story",
                pygame.K_o: "original_kroz_trilogy",
            }

            if event.key in transition_map:
                self.sm.transition(transition_map[event.key])
