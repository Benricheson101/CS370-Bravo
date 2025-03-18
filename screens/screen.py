from constants import BLACK, LIGHTBLUE, LIGHTGRAY, WHITE
from renderer.cell_grid import CellGrid


def color_menu(g: CellGrid):
    # Color = true;
    g.bak(BLACK, BLACK);
    g.clrscr()
    # bor(3);
    # cur(3);
    g.col(LIGHTBLUE, LIGHTBLUE)
    g.gotoxy(33,3)
    g.write('RETURN TO KROZ')
    g.gotoxy(18,10);
    g.col(WHITE, LIGHTGRAY)
    g.write('Is your screen Color or Monochrome (C/M)? C');
    # g.gotoxy(wherex-1,wherey);cur(2);
    # read(kbd,ch);
    # if upcase(ch)='M' then
    # begin
    # textmode(BW80);
    # Color := false;
    # end
    # else Color := true;
    g.bak(BLACK,BLACK);
    g.gotoxy(18,10);
    # g.delline;
    g.gotoxy(9,17);
    g.col(LIGHTGRAY,LIGHTGRAY);
    g.write('If you have an older PC (like an XT model) choose "S" for Slow.');
    g.gotoxy(10,19);
    g.write('If you have a PC AT, 80386 chip, etc., choose "F" for Fast.');
    g.gotoxy(32,21);
    g.write('(Default = Slow)');
    g.col(WHITE,WHITE);
    g.gotoxy(28,14);
    g.write('Slow or Fast PC (S/F)? S');
    # g.gotoxy(wherex-1,wherey);
    # read(kbd,ch);
    # if upcase(ch) = 'F' then FastPC := true else FastPC := false;
    # clrscr;
