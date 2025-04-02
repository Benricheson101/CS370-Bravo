import pygame
from pygame.event import Event
from constants import BLACK, BLUE, LIGHTCYAN, LIGHTGRAY, LIGHTGREEN, LIGHTRED, RED, SCREEN_SIZE, WHITE, YELLOW
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

class DifficultyScreen(State):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        g = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLUE,
            game=sm.game,
        )

        self.grid = g

        # g.bg = BLUE
        g.bak(BLUE, BLACK);#bor(4)
        g.clrscr();g.cur(3)
        g.gotoxy(32,1)
        g.col(RED,LIGHTGRAY);g.bak(BLUE,BLACK)
        g.write('ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ')
        g.gotoxy(32,3)
        g.write('ßßßßßßßßßßßßßßßß')
        g.gotoxy(25,5);g.col(WHITE, WHITE)
        g.write('An Apogee Software Production')
        g.gotoxy(28,7)
        g.write('Created by Scott Miller')
        g.gotoxy(1,9);g.col(LIGHTCYAN,LIGHTGRAY)
        g.writeln('  In your search for the precious Crown within the mysterious kingdom of Kroz')
        g.writeln('  you have blundered upon a secret passage leading deep into the Earth.  With')
        g.writeln('  your worn lantern you journey downward void of fear,  sweat beading on your')
        g.writeln('  forehead as you anticipate great treasures.  Undoubtedly, the Crown must be')
        g.writeln('  guarded by unspeakable dangers.  Still, armed with a whip and great courage')
        g.writeln('           you decide to continue your quest, and journey downward...')
        g.gotoxy(1,17);g.col(LIGHTGREEN,LIGHTGRAY)
        g.write('         Use the cursor keys to move yourself (')
        g.col(YELLOW, WHITE);g.write(chr(2));g.col(LIGHTGREEN,LIGHTGRAY)
        g.writeln(') through the kingdom.')
        g.writeln('            Use your whip (press W) to destroy all nearby creatures.')
        g.writeln('       You are on your own to discover what other mysteries await--some')
        g.writeln('                           helpful, others deadly...')
        g.col(YELLOW,LIGHTGRAY)
        g.gotoxy(13,22)
        g.write('Are you a ');g.col(WHITE,WHITE);g.write('N');g.col(YELLOW,LIGHTGRAY)
        g.write('ovice, an ');g.col(WHITE, WHITE);g.write('E');g.col(YELLOW, LIGHTGRAY)
        g.write('xperienced or an ');g.col(WHITE, WHITE);g.write('A');g.col(YELLOW, LIGHTGRAY)
        g.write('dvanced player?')
        g.col(LIGHTRED,BLACK);#g.write(chr(219)); # TODO the col() should flash
        g.bak(RED, LIGHTGRAY)
        #g.gotoxy(32,2);#g.col(randint(0, 16),0);write(' RETURN TO KROZ ');delay(50)
        g.flash(32, 2, ' RETURN TO KROZ ')

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        return super().handle_event(event)
