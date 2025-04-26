from random import randint
import pygame
from pygame.event import Event
from constants import BLUE
from util.state import State, StateMachine
from Sound import SoundEffects

SHAREWARE_WAIT = pygame.event.custom_type()

class SharewareScreen(State):
    wait: bool

    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        self.sound_effects = SoundEffects()
        
        self.grid.fill = BLUE
        self.wait = False

        self.grid.bak(1,0);self.grid.clrscr();self.grid.cur(3);self.grid.col(15,15);
        self.grid.gotoxy(24,1);
        self.grid.writeln('RETURN TO KROZ Ä HOW TO REGISTER');
        self.grid.gotoxy(1,2);
        for _ in range(79): self.grid.write("Ä")
        self.grid.gotoxy(1,3);
        self.grid.col(7,7);
        self.grid.writeln('  This is Volume I of the Super Kroz Trilogy.  Return to Kroz is a shareware');
        self.grid.writeln('game, which means it is user supported.  If you enjoy this game you are asked');
        self.grid.writeln('by the author to please send an appreciation check of $7.50 to Apogee Software.');
        self.grid.writeln('This minimal amount will help compensate the many months of work that went into');
        self.grid.writeln('the creation of this game.');
        self.grid.writeln('  Also, this registration fee will allow you to order the two non-shareware');
        self.grid.write  ('sequels:  ');self.grid.col(15,9);
        self.grid.write  ('Temple of Kroz');self.grid.col(7,7);
        self.grid.write  (' (Volume II) and ');self.grid.col(15,9);
        self.grid.write  ('The Last Crusade of Kroz');self.grid.col(7,7);
        self.grid.writeln(' (Volume III).');
        self.grid.writeln('Each sequel can be ordered for $7.50 each, or all three for $20.  Registered');
        self.grid.writeln('players will also get a secret code that makes this game easier to complete,');
        self.grid.writeln('plus a "Hints, Tricks and Scoring Secrets" guide and "The Domain of Kroz" map.');
        self.grid.writeln('  The three original Kroz games are also available and have been updated with');
        self.grid.write  ('improved features.  All three of the original Kroz games (');self.grid.col(15,9);
        self.grid.write  ('Kingdom of Kroz');self.grid.col(7,7);
        self.grid.writeln(',');self.grid.col(15,9);
        self.grid.write  ('Caverns of Kroz');self.grid.col(7,7);
        self.grid.write  (', ');self.grid.col(15,9);
        self.grid.write  ('Dungeons of Kroz');self.grid.col(7,7);
        self.grid.writeln(') are $7.50 each or $15 for all three. Kingdom');
        self.grid.writeln('of Kroz recently won "Best Game" in a national contest.  These first three');
        self.grid.writeln('Kroz games feature 95 new levels to explore.');
        self.grid.writeln;
        self.grid.write('Please make checks payable to:');
        self.grid.col(14,7);
        self.grid.writeln('   Apogee Software    (phone: 214/240-0614)');self.grid.gotoxy(31,20);
        self.grid.writeln('   4206 Mayflower');self.grid.gotoxy(31,21);
        self.grid.writeln('   Garland, TX 75043');
        self.grid.writeln;
        self.grid.col(7,7);
        self.grid.writeln('Thank you and enjoy the game.  -- Scott Miller (author)');

        self.grid.bak(0,0);self.grid.clrscr;self.grid.cur(3);

    def enter(self, **kwargs):
        self.wait = kwargs["wait"] if "wait" in kwargs else False
        if self.wait:
            pygame.time.set_timer(SHAREWARE_WAIT, 3333, loops=1)

    def handle_event(self, event: Event):
        if event.type == SHAREWARE_WAIT:
            self.wait = False

            self.sound_effects.intr_continue()
            self.grid.bak(randint(0, 6)+1,7);
            self.grid.gotoxy(1,25);
            self.grid.insline()
            self.grid.gotoxy(27,25);
            self.grid.col(16,16);
            self.grid.write('Press any key to continue.');

        elif event.type == pygame.KEYDOWN:
            if not self.wait:
                self.sm.transition("main_menu")
