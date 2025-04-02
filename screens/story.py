import pygame
from pygame.event import Event
from constants import BLUE, SCREEN_SIZE
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

class StoryScreen(State):
    def __init__(self, sm: "StateMachine") -> None:
        super().__init__(sm)

        g = CellGrid(
            grid_size=SCREEN_SIZE,
            fill=BLUE,
            game=sm.game,
        )

        self.grid = g

        # g.bg = BLUE
        g.bak(1,0)
        g.clrscr()
        g.cur(3)
        g.gotoxy(29,2);g.col(14,7);g.writeln('THE STORY BEHIND KROZ')
        g.gotoxy(29,3);            g.writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
        g.writeln()
        g.col(15,7)
        g.writeln('   The original Kroz Trilogy (consisting of Caverns of Kroz, Dungeons of Kroz,')
        g.writeln(' and Kingdom of Kroz) was developed after I spent many hours playing another')
        g.writeln(' explore-the-levels type game titled Rogue.  I never could finish Rogue,')
        g.writeln(' though, because the game relied too much on luck and random occurrences.')
        g.writeln('   The name "Kroz" is actually Zork (an Infocom text adventure) spelled in')
        g.writeln(' reverse.  Many players still inquire about this bit of trivia.  The game was')
        g.writeln(' first designed without predefined level layouts, meaning every level was a')
        g.writeln(' random placement of creatures and play field objects.  New objects, like')
        g.writeln(' spells, lava, doors, etc., were added quickly as the first Kroz game took')
        g.writeln(' shape, including the ability to have predefined level floor plans.')
        g.writeln('   One of my objects was to create a game that wasn\'t all fast paced action,')
        g.writeln(' but also included strategy and puzzle solving.  Kingdom of Kroz was entered')
        g.writeln(' in a national programming contest in 1988 and took top honors in the game')
        g.writeln(' category, and number two overall (beat out by a spreadsheet program).')
        g.writeln('   The latest Kroz Trilogy has been greatly re-designed and re-programmed, but')
        g.writeln(' the familiar appearance has been mostly maintained.  You will discover new')
        g.writeln(' dangers, creatures and objects in your adventures below.  Good luck...')
        g.writeln('   The latest Kroz game, The Lost Adventures of Kroz, came about as a direct')
        g.writeln(' result of players requesting more, more, more Kroz!  So I delivered the goods.')
        g.flash(27,25,'Press any key to continue.')

    def render(self, screen):
        self.grid.render(screen)

    def update(self, **kwargs):
        self.grid.update(**kwargs)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            # self.sm.transition(InstructionsPage2(self.sm))
            self.sm.transition("main_menu")
