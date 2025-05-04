import json
import os
from typing import List

from pygame import Surface
import pygame
from pygame.event import Event
from constants import BLACK, GAME_GRID_COLS, GAME_GRID_ROWS
from renderer.cell_grid import CellGrid
from screens.game import Scoreboard
from util.path import exe_rel
from util.state import State, StateMachine

# high scores are stored in return.hs using JSON: [{name: string; high_score: int; high_level: int}]

# DEFAULT_SCORES = """
# [
#     {"name": "Scott Miller", "high_score": 10963, "high_level": 11},
#     {"name": "I. Jones", "high_score": 4281, "high_level": 5},
# """ \
#     + ",".join(["""{"name": "-----", "high_score": 0, "high_level": 0}""" for _ in range(13)]) \
#     + "]"

BLANK_SCORES = [{"name": "-----", "high_score": 0, "high_level": 0} for _ in range(15)]

DEFAULT_SCORES = [
    {"name": "Scott Miller", "high_score": 10963, "high_level": 11},
    {"name": "I. Jones", "high_score": 4281, "high_level": 5},
] + BLANK_SCORES

class HighScoreScreen(State):
    high_scores: List
    is_typing: bool
    typed: str

    def __init__(self, sm: "StateMachine") -> None:
        super().__init__(sm)
        self.scoreboard = Scoreboard(sm.game)

        self.grid = CellGrid(
            grid_size=(GAME_GRID_COLS+2, GAME_GRID_ROWS+2),
            fill=BLACK,
            game=sm.game,
        )
        self.grid.border()

    def update(self, **kwargs):
        self.grid.update(**kwargs)
        self.scoreboard.update(**kwargs)

    def render(self, screen: Surface):
        self.grid.render(screen)
        self.scoreboard.render(screen)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if not self.is_typing:
                if self.state == "play_again":
                    if event.key == pygame.K_y:
                        self.sm.game.reset_game()
                        self.sm.transition("difficulty")
                        return
                    self.sm.transition("shareware", wait=False)

                elif self.state == "quit":
                    self.sm.transition("shareware", wait=False)
                return

            if event.key == pygame.K_RETURN:
                if len(self.typed) == 0:
                    return

                self.is_typing = False
                self.current["name"] = self.typed
                with open(exe_rel("./highscore.json"), "w") as f:
                    f.write(
                        json.dumps(
                            [s for s in self.high_scores if s["high_score" ]> 0]
                        )
                    )

                self.grid.cur(3)
                self.grid.bak(0,0)
                self.grid.gotoxy(15,23)
                self.grid.write('                                   ')

                if self.play_again:
                    self.grid.flash(14,25,"Do you want to play another game? (Y/N)")
                    self.state = "play_again"
                else:
                    self.grid.flash(21,25,"Press any key to continue.")
                    self.state = "quit"

            elif event.key == pygame.K_BACKSPACE:
                self.grid.gotoxy(self.grid.cur_pos[0], self.grid.cur_pos[1]+1)
                self.grid.bak(4,7)
                self.grid.write(" ")
                self.grid.gotoxy(self.grid.cur_pos[0], self.grid.cur_pos[1]+1)
                self.typed = self.typed[:-1]
            else:
                self.grid.write(event.unicode)
                self.typed += event.unicode

    def enter(self, **kwargs):
        self.is_typing = False
        self.typed = ""
        self.state = "enter"

        high_scores: List = []
        self.play_again = kwargs["play_again"] if "play_again" in kwargs else True
        print("play again:", self.play_again)

        try:
            with open(exe_rel("./highscore.json"), "r") as f:
                high_scores = json.loads(f.read()) + BLANK_SCORES
        except FileNotFoundError as e:
            print("faied to open hs file", e)
            high_scores = DEFAULT_SCORES.copy()
        except json.JSONDecodeError:
            print("failed to decode highscore file")
            os.remove("./highscore.json")
            high_scores = DEFAULT_SCORES.copy()

        self.current = {
            "name": "",
            "high_score": self.sm.game.score,
            "high_level": self.sm.game.current_level,
        }
        high_scores.append(self.current)
        high_scores.sort(key=lambda a: a["high_score"], reverse=True)
        place = high_scores.index(self.current)

        self.high_scores = high_scores

        self.grid.col(9,9);
        self.grid.gotoxy(28,3);
        self.grid.write('RETURN TO KROZ');
        self.grid.col(11,7);
        self.grid.gotoxy(16,5);self.grid.write('NAME');
        self.grid.gotoxy(33,5);self.grid.write('HIGH SCORE');
        self.grid.gotoxy(49,5);self.grid.write('LEVEL');

        for i, item in enumerate(high_scores[:15]):
            if i % 2:
                self.grid.col(12, 7)
            else:
                self.grid.col(13, 7)

            self.grid.gotoxy(13, i+6)
            self.grid.write(str(i+1)) # what is x:2 in pascal?

            self.grid.gotoxy(16, i+6)
            self.grid.write(item["name"])

            self.grid.gotoxy(36, i+6)
            self.grid.write(item["high_score"])

            self.grid.gotoxy(50, i+6)
            self.grid.write(item["high_level"])

        if place < 15:
            self.grid.bak(4,7)
            self.grid.gotoxy(16, place+6)
            self.grid.write('               ');
            self.grid.col(4,0);
            self.grid.bak(7,7);
            self.grid.gotoxy(15,23);
            self.grid.write('Enter your name then press <enter>.');
            self.grid.col(15,15);
            self.grid.bak(4,7);
            self.grid.gotoxy(16,place+6);
            self.grid.cur(2);
            self.is_typing = True
        else:
            self.grid.flash(14,25,"Do you want to play another game? (Y/N)")
            self.state = "play_again"

    def exit(self):
        self.grid.clrscr()
