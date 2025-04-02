import pygame
from pygame.event import Event
from constants import BLUE, SCREEN_SIZE
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

class MarketingScreen(State):
    def __init__(self, sm: "StateMachine") -> None:
        super().__init__(sm)

        g = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLUE,
            game=sm.game,
        )

        self.grid = g

        # g.bor(10)
        # g.bg = BLUE
        g.bak(1,0)
        g.clrscr()
        # g.ClearKeys
        # g.cur(3)
        g.gotoxy(29,2);g.col(14,7);g.writeln('THE MARKETING OF KROZ')
        g.gotoxy(29,3);            g.writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
        g.writeln()
        g.col(15,7)
        g.writeln('   Return to Kroz is a user-supported game.  This means that the creator of')
        g.writeln(' this program relies on the appreciation of honest players to pay the game\'s')
        g.writeln(' minimal registration fee--$7.50.')
        g.writeln('   Payment of this fee entitles you to all the free help and hints you might')
        g.writeln(' need to enjoy the game.  All letters from registered users are answered')
        g.writeln(' within two days.  (Try to get this kind of support from commercial games!)')
        g.writeln('   Also, players can order the other Kroz sequels ONLY if this first')
        g.writeln(' registration fee is paid.  ($7.50 each or $20 for all three games.)')
        g.writeln('   Everyone who orders (or registers) all three of the Super Kroz Trilogy also')
        g.writeln(' get a "Hints, Tricks and Scoring Secrets" guide, and "The Domain of Kroz" map.')
        g.writeln('   A single Kroz games takes nearly six months to create, or, over 200 hours!')
        g.writeln(' I can\'t afford to devote this much time without receiving something in return.')
        g.writeln(' That is why I ask for this small fee, which is only necessary if you enjoy')
        g.writeln(' this game.  In other words, try before you buy.')
        g.writeln('   Even if you buy this game from a public domain or shareware library, I don\'t')
        g.writeln(' receive any of that money.  You\'re simply paying for "storage, distribution,')
        g.writeln(' disk, and handling".')
        g.writeln
        g.writeln('   -- Scott Miller, President, Apogee Software Productions')
        g.flash(27,25,'Press any key to continue.')

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            # self.sm.transition(InstructionsPage2(self.sm))
            self.sm.transition("main_menu")

