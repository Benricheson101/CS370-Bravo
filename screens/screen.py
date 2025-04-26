import pygame
from pygame.event import Event
from constants import BLACK, LIGHTBLUE, LIGHTGRAY, WHITE
from util.state import State, StateMachine
from Sound import SoundEffects

class ColorMenu(State):
    has_chosen_color: bool

    def __init__(self, sm: StateMachine) -> None:
        super().__init__(sm)

        self.has_chosen_color = False

        self.sound_effects = SoundEffects()
        
        self.grid.bak(BLACK, BLACK)
        self.grid.clrscr()
        # bor(3)
        self.grid.cur(3)
        self.grid.col(LIGHTBLUE, LIGHTBLUE)
        self.grid.gotoxy(33,3)
        self.grid.write('RETURN TO KROZ')
        self.grid.gotoxy(18,10)
        self.grid.col(WHITE, LIGHTGRAY)
        self.grid.write('Is your screen Color or Monochrome (C/M)? C')
        # self.grid.gotoxy(wherex-1,wherey);cur(2)

        self.grid.gotoxy(self.grid.cur_pos[0], self.grid.cur_pos[1]+1);self.grid.cur(2)

        # read(kbd,ch)
        # if upcase(ch)='M' then
        # begin
        # textmode(BW80)
        # Color := false
        # end
        # else Color := true

        # self.grid.gotoxy(18,13)
        # self.grid.write("asdf")
        # self.grid.gotoxy(25,16)
        # self.grid.write("asdf")

        # self.grid.bak(BLACK,BLACK)
        # self.grid.gotoxy(18,10)
        # self.grid.delline()
        # self.grid.gotoxy(9,17)
        # self.grid.col(LIGHTGRAY,LIGHTGRAY)
        # self.grid.write('If you have an older PC (like an XT model) choose "S" for Slow.')
        # self.grid.gotoxy(10,19)
        # self.grid.write('If you have a PC AT, 80386 chip, etc., choose "F" for Fast.')
        # self.grid.gotoxy(32,21)
        # self.grid.write('(Default = Slow)')
        # self.grid.col(WHITE,WHITE)
        # self.grid.gotoxy(28,14)
        # self.grid.write('Slow or Fast PC (S/F)? S')

        # self.grid.gotoxy(wherex-1,wherey)
        # read(kbd,ch)
        # if upcase(ch) = 'F' then FastPC := true else FastPC := false
        # clrscr

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if not self.has_chosen_color:
                self.sm.game.color = event.key == pygame.K_m
                self.has_chosen_color = True

                self.grid.bak(BLACK,BLACK)
                self.grid.gotoxy(18,10)
                self.grid.delline()
                self.grid.gotoxy(9,17)
                self.grid.col(LIGHTGRAY,LIGHTGRAY)
                self.grid.write('If you have an older PC (like an XT model) choose "S" for Slow.')
                self.grid.gotoxy(10,19)
                self.grid.write('If you have a PC AT, 80386 chip, etc., choose "F" for Fast.')
                self.grid.gotoxy(32,21)
                self.grid.write('(Default = Slow)')
                self.grid.col(WHITE,WHITE)
                self.grid.gotoxy(28,14)
                self.grid.write('Slow or Fast PC (S/F)? S')
                self.grid.gotoxy(self.grid.cur_pos[0], self.grid.cur_pos[1]+1)
                self.sound_effects.intr_low()
                
            else:
                self.sm.game.fastpc = event.key == pygame.K_f
                self.sm.transition("difficulty")
