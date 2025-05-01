from typing import TYPE_CHECKING
from pygame import Surface
from constants import BLACK, BLUE, GAME_GRID_COLS, GAME_GRID_ROWS, GAME_GRID_WIDTH, GRID_CELL_WIDTH, SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS
from renderer.cell_grid import CellGrid
from util.state import State, StateMachine

import pygame

# and somewhere at top
from level.level_load import save_level, restore_level  # assuming save/restore are here

if TYPE_CHECKING:
    from game import Game

class GameScreen(State):
    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        self.game = sm.game

        self.grid = CellGrid(
            grid_size=(GAME_GRID_COLS+2, GAME_GRID_ROWS+2),
            fill=BLACK,
            game=sm.game,
        )
        self.grid.border()

        self.scoreboard = Scoreboard(sm.game)

        self.game_grid = self.grid # cus some other stuff uses game_grid

        self.current_level = 1

        self.load_current_level()

        self.grid._flip_blink()

        self.pause_reason = None

    def enter(self, **kwargs):
        self.pause(True)
        self.pause_reason = "enter"
        self.grid.flash(16,25,'Press any key to begin this level.');


    def update(self, **kwargs):
        self.grid.update(paused=self.paused, **kwargs)
        self.scoreboard.update(paused=self.paused, **kwargs)

    def render(self, screen: Surface):
        self.grid.render(screen)
        self.scoreboard.render(screen)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if self.paused:
                if event.key == pygame.K_y and self.pause_reason == "quit":
                    self.sm.transition("shareware", wait=False)
                    return
                elif event.key == pygame.K_y and self.pause_reason == "save":
                    save_level(self.grid)
                elif event.key == pygame.K_y and self.pause_reason == "restore":
                    restore_level(self.grid)

                self.grid.restore_border()
                self.pause(False)
                self.pause_reason = None

            if event.key == pygame.K_s:
                if not self.paused:
                    self.pause_reason = "save"
                    self.grid.flash(16,25,'Are you sure you want to SAVE (Y/N)?')
                    self.pause(True)
            elif event.key == pygame.K_r:
                if not self.paused:
                    self.pause_reason = "restore"
                    self.grid.flash(16,25,'Are you sure you want to RESTORE (Y/N)?')
                    self.pause(True)
            elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                if not self.paused:
                    self.pause_reason = "quit"
                    self.grid.flash(16,25,'Are you sure you want to quit (Y/N)?')
                    self.pause(True)

    def load_current_level(self):
            # Check for even-numbered levels (randomly generated)
            if self.game.current_level % 2 == 0 and self.game.current_level != 20:
                from level.level_load import random_level
                random_level(self.game_grid, self.game.current_level)
            else:
                from level.level_load import load_level
                load_level(self.game, self.grid, self.game.current_level)


class Scoreboard(CellGrid):
    def __init__(self, game: "Game"):
        super().__init__(
            grid_size=(SCOREBOARD_GRID_COLS, SCOREBOARD_GRID_ROWS),
            offset=(GAME_GRID_WIDTH + GRID_CELL_WIDTH * 2, 0),
            fill=BLUE,
            game=game,
        )

        self.col(14,7);
        self.print(5,1,'Score');
        self.print(5,4,'Level');
        self.print(5,7,'Gems');
        self.print(5,10,'Whips');
        self.print(3,13,'Teleports');
        self.print(5,16,'Keys');
        self.col(11,7);self.bak(4,0);
        self.print(4,19,'OPTIONS');
        self.bak(1,0);
        self.gotoxy(4,20);self.col(15,15);self.write('W');self.col(7,7);self.write('hip');
        self.gotoxy(4,21);self.col(15,15);self.write('T');self.col(7,7);self.write('eleport');
        self.gotoxy(4,22);self.col(15,15);self.write('P');self.col(7,7);self.write('ause');
        self.gotoxy(4,23);self.col(15,15);self.write('Q');self.col(7,7);self.write('uit');
        self.gotoxy(4,24);self.col(15,15);self.write('S');self.col(7,7);self.write('ave');
        self.gotoxy(4,25);self.col(15,15);self.write('R');self.col(7,7);self.write('estore');

    def update(self, **kwargs):
        super().update()

        map = {
            2: self.game.score,
            5: self.game.current_level,
            8: self.game.gem_count,
            11: self.game.whip_count,
            14: self.game.teleport_count,
            17: self.game.key_count,
        }

        self.bak(7,0)
        self.col(4,7);

        for ypos, val in map.items():
            if ypos == 8:
                self.col(20, 23)

            self.gotoxy(4, ypos)
            self.write('       ')

            strval = str(val)



            # TODO: whip power
            # elif ypos == 11:
            #     if self.game.whip_power >= 4 and self.game.whip_power <= 5:
            #         strval += "+"
            #     elif self.game.whip_power > 5:
            #         strval += "++"

            self.gotoxy(7 - len(strval) // 2, ypos)
            self.write(strval)

            if ypos == 8:
                self.col(4, 7)

        self.bak(0, 0)
