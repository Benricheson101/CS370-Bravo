import pygame
from pygame.event import Event
from constants import BLACK, BLUE, LIGHTCYAN, LIGHTGRAY, LIGHTGREEN, RED, WHITE, YELLOW
from util.state import State, StateMachine
from Sound import SoundEffects

class DifficultyScreen(State):
    done: bool

    def __init__(self, sm: StateMachine) -> None:

        super().__init__(sm)

        self.done = False

        self.grid.fill = BLUE
        
        self.sound_effects = SoundEffects()

        self.grid.bak(BLUE, BLACK)
        self.grid.clrscr();self.grid.cur(3)
        self.grid.gotoxy(32,1)
        self.grid.col(RED,LIGHTGRAY);self.grid.bak(BLUE,BLACK)
        self.grid.write('ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ')
        self.grid.gotoxy(32,3)
        self.grid.write('ßßßßßßßßßßßßßßßß')
        self.grid.gotoxy(25,5);self.grid.col(WHITE, WHITE)
        self.grid.write('An Apogee Software Production')
        self.grid.gotoxy(28,7)
        self.grid.write('Created by Scott Miller')
        self.grid.gotoxy(1,9);self.grid.col(LIGHTCYAN,LIGHTGRAY)
        self.grid.writeln('  In your search for the precious Crown within the mysterious kingdom of Kroz')
        self.grid.writeln('  you have blundered upon a secret passage leading deep into the Earth.  With')
        self.grid.writeln('  your worn lantern you journey downward void of fear,  sweat beading on your')
        self.grid.writeln('  forehead as you anticipate great treasures.  Undoubtedly, the Crown must be')
        self.grid.writeln('  guarded by unspeakable dangers.  Still, armed with a whip and great courage')
        self.grid.writeln('           you decide to continue your quest, and journey downward...')
        self.grid.gotoxy(1,17);self.grid.col(LIGHTGREEN,LIGHTGRAY)
        self.grid.write('         Use the cursor keys to move yourself (')
        self.grid.col(YELLOW, WHITE);self.grid.write(chr(2));self.grid.col(LIGHTGREEN,LIGHTGRAY)
        self.grid.writeln(') through the kingdom.')
        self.grid.writeln('            Use your whip (press W) to destroy all nearby creatures.')
        self.grid.writeln('       You are on your own to discover what other mysteries await--some')
        self.grid.writeln('                           helpful, others deadly...')
        self.grid.col(YELLOW,LIGHTGRAY)
        self.grid.gotoxy(13,22)
        self.grid.write('Are you a ');self.grid.col(WHITE,WHITE);self.grid.write('N');self.grid.col(YELLOW,LIGHTGRAY)
        self.grid.write('ovice, an ');self.grid.col(WHITE, WHITE);self.grid.write('E');self.grid.col(YELLOW, LIGHTGRAY)
        self.grid.write('xperienced or an ');self.grid.col(WHITE, WHITE);self.grid.write('A');self.grid.col(YELLOW, LIGHTGRAY)
        self.grid.write('dvanced player?')
        self.grid.col(28, 16);self.grid.write(chr(219))
        self.grid.bak(RED, LIGHTGRAY)
        self.grid.gotoxy(32,2)
        self.grid.flash(32, 2, ' RETURN TO KROZ ')

    def handle_event(self, event: Event):
        difficulty_map = {
            pygame.K_n: 8,
            pygame.K_SPACE: 8,
            pygame.K_RETURN: 8,
            pygame.K_e: 5,
            pygame.K_a: 2,
            pygame.K_EXCLAIM: 9,
        }

        if event.type == pygame.KEYDOWN:
            if self.done:
                self.sm.transition("shareware", wait=True)
                return

            cont = False
            if event.key in difficulty_map:
                self.sm.game.difficulty = difficulty_map[event.key]
                cont = True
                self.sound_effects.intr_high()
            elif event.key == pygame.K_1 and pygame.key.get_mods() & (pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT): # shift + 1 = !
                self.sm.game.difficulty = 9
                cont = True
                self.sound_effects.intr_high()

            if cont:
                self.sound_effects.intr_middle()
                self.grid.gotoxy(13,22);self.grid.col(0,0);self.grid.bak(1,0)
                for _ in range(28):
                    self.grid.write("  ")

                mode = self.sm.game.difficulty

                self.grid.col(30,31);self.grid.bak(1,0)
                if mode == 8: 
                    self.grid.gotoxy(37,22);self.grid.write("NOVICE")
                    self.sm.game.gem_count = 25
                    self.sm.game.whip_count = 10
                elif mode == 5: 
                    self.grid.gotoxy(34,22);self.grid.write("EXPERIENCED")
                    self.sm.game.gem_count = 18
                elif mode == 2: 
                    self.grid.gotoxy(34,22);self.grid.write("ADVANCED")
                    self.sm.game.gem_count = 10
                elif mode == 9: 
                    self.grid.gotoxy(34,22);self.grid.write("SECRET MODE")
                    self.sm.game.gem_count = 250
                    self.sm.game.whip_count = 100
                    self.sm.game.teleport_count = 50
                    self.sm.game.key_count = 1
                    self.sm.game.whip_power = 3
                self.grid.gotoxy(33,25)
                self.grid.col(7,7)
                self.grid.write("Press any key.")
                self.grid.bak(4,7)

                self.done = True
