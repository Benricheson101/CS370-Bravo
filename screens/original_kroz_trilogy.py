from pygame import KEYDOWN
from pygame.event import Event
from constants import BLUE
from util.state import State, StateMachine


class OriginalKrozTrilogyScreen(State):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        self.grid.fill = BLUE

        # self.grid.bor(15); # what is bor?
        self.grid.bak(1,0)
        self.grid.clrscr()
        self.grid.cur(3)
        self.grid.gotoxy(27,2);self.grid.col(14,7);self.grid.writeln('THE ORIGINAL KROZ TRILOGY')
        self.grid.gotoxy(27,3);                    self.grid.writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
        self.grid.writeln()
        self.grid.col(15,7)
        self.grid.writeln('   The original three Kroz games were such a tremendous success that I was')
        self.grid.writeln(' obliged to make this second, and probably final trilogy.  The first three')
        self.grid.writeln(' Kroz games are:   þ Kingdom of Kroz  þ Caverns of Kroz  þ Dungeons of Kroz.')
        self.grid.writeln(' All three are still available and are constantly being updated and improved.')
        self.grid.writeln('   The original Kroz Trilogy games can be purchased for $7.50 each, or all 3')
        self.grid.writeln(' for $15 (these prices include postage, disks, and handling).')
        self.grid.writeln('   Only Kingdom of Kroz can be placed in a shareware library for distribution,')
        self.grid.writeln(' and the other two can only be ordered from Apogee Software Productions.')
        self.grid.writeln('   To purchase these games please make checks payable to Apogee Software, and')
        self.grid.writeln(' mail to:  4206 Mayflower ù Garland, TX 75043.  Call 214/240-0614 for info.')
        self.grid.writeln(' This address will always be valid, but you can call to verify if you need to.')
        self.grid.writeln('   These Kroz games feature a total of 95 new, unique levels.  Kingdom of Kroz')
        self.grid.writeln(' took the title of "Best Game" in a 1988 national programming competition.')
        self.grid.writeln('   All Kroz games work on all monitors, either graphics or monochrome systems.')
        self.grid.writeln(' Plus, they only rely on keyboard control, and have slow-down routines that')
        self.grid.writeln(' permit them to function correctly on any speed IBM PC compatible computer.')
        self.grid.writeln('   ASP also sells an "Adventure FUN-PAK", that contains four games that are')
        self.grid.writeln(" similar to the Kroz games in style.  This FUN-PAK (there's also a \"Puzzle\"")
        self.grid.writeln(' FUN-PAK" avalaible) is sold for $10, which includes shipping.  Thank you.')
        self.grid.flash(27,25,'Press any key to continue.')

    def handle_event(self, event: Event):
        if event.type == KEYDOWN:
            self.sm.transition("main_menu")
