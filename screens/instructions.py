import pygame
from pygame.event import Event
from constants import BLACK, BLUE, LIGHTGRAY, SCREEN_SIZE, WHITE, YELLOW
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

class InstructionsPage1(State):
    def __init__(self, sm: "StateMachine") -> None:
        super().__init__(sm)

        g = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLUE,
            game=sm.game,
        )

        self.grid = g

        # g.bg = BLUE
        g.bak(BLUE,BLACK)
        # g.bor(4)
        g.clrscr()
        # g.cur(3)
        # g.ClearKeys
        g.gotoxy(32,2);g.col(YELLOW,LIGHTGRAY);g.writeln('THE INSTRUCTIONS')
        g.gotoxy(32,3);          g.writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
        g.writeln()
        g.col(WHITE,LIGHTGRAY)
        g.writeln('   Return to Kroz is a game of exploration and survival.  Your journey will')
        g.writeln(' take you through 20 very dangerous chambers, each riddled with diabolical')
        g.writeln(' traps and hideous creatures.   Hidden in the deepest dungeon lies the')
        g.writeln(' priceless Crown of Kroz--your quest. Use the cursor pad to move 8 directions.')
        g.writeln('   The chambers contain dozens of treasures, spells, traps and other unknowns.')
        g.writeln(' Touching an object for the first time will reveal a little of its identity,')
        g.writeln(' but it will be left to you to decide how best to use it--or avoid it.')
        g.writeln('   When a creature touches you it will vanish, taking with it a few of your')
        g.writeln(' gems that you have collected. If you have no gems then the creature will')
        g.writeln(' instead take your life!  Whips can be used to kill nearby creatures, but')
        g.writeln(' they\'re better used to smash through "crumbled walls" and other terrain.')
        g.writeln('   PCjr players can use')
        g.writeln(' the alternate cursor                 U I O      ( NW N NE )')
        g.writeln(' pad instead of the cursor             J K       (   W E   )')
        g.writeln(' keys to move your man, and           N M ,      ( SW S SE )')
        g.writeln(' the four normal cursor keys.')
        g.writeln('   It\'s a good idea to save your game at every new level, therefore, if you die')
        g.writeln(' you can easily restore the game at that level and try again.')
        g.writeln('   Registered users can request a "Hidden Tricks and Hints" sheet if needed.')
        g.flash(27,25,'Press any key to continue.')
        g.bak(BLUE,BLACK)

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            # self.sm.transition(InstructionsPage2(self.sm))
            self.sm.transition("instructions_2")


# def instructions2(g: CellGrid):
class InstructionsPage2(State):
    def __init__(self, sm: "StateMachine") -> None:
        super().__init__(sm)

        g = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLUE,
            game=sm.game,
        )

        self.grid = g

        # g.bg = BLUE
        g.clrscr()
        # g.cur(3)
        # g.ClearKeys
        g.gotoxy(32,2);g.col(YELLOW,LIGHTGRAY);g.writeln('THE INSTRUCTIONS')
        g.gotoxy(32,3);          g.writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
        g.writeln()
        g.col(WHITE,LIGHTGRAY)
        g.writeln('   Return to Kroz will present you with many challenges.  You will venture deep')
        g.writeln(' underground and probably not make it out alive!')
        g.writeln()
        g.writeln(' Hints:  þ Use your player to touch each new object to find out about it.  When')
        g.writeln('           you first touch an object a message appears at the bottom of the')
        g.writeln('           screen that describes it.')
        g.writeln('       þþ> Don\'t forget to use the Home, End, PgUp, and PgDn keys to move your')
        g.writeln('           on-screen character diagonally (along with the marked cursor keys).')
        g.writeln('         þ Collect keys to unlock doors, which usually block the stairs going.')
        g.writeln('         þ The faster monsters are the most dangerous to touch--they will knock')
        g.writeln('           off three of your valuable gems.  The slowest creatures only take a')
        g.writeln('           single gem from you, and the medium speed monsters take two.')
        g.writeln('         þ Nearly every new level presents you with new objects to discover.')
        g.writeln()
        g.writeln('   To prove to you that this game CAN be completed, let me say (or brag) that I')
        g.writeln(' have finished this game on the "Advanced" skill level, with over 120 gems and')
        g.writeln(' 60 whips left to spare.  On the "Novice" level I can play and win one handed!')
        g.writeln('   There\'s many secret tricks in this game that can help you (even on Level 1)')
        g.writeln(' but even without these hidden maneuvers you can complete Return to Kroz.')
        g.flash(27,25,'Press any key to continue.')

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            # self.sm.transition(InstructionsPage2(self.sm))
            self.sm.transition("main_menu")

