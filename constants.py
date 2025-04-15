# TODO: try to make this scale automatically based on display size
from pygame import Color
import pygame


SCALE = 2

# The size of a single grid cell
GRID_CELL_HEIGHT = int(16 * SCALE)
GRID_CELL_WIDTH = int(9 * SCALE)

# game grid
GAME_GRID_ROWS = 23
GAME_GRID_COLS = 64

GAME_GRID_HEIGHT = GAME_GRID_ROWS * GRID_CELL_HEIGHT
GAME_GRID_WIDTH = GAME_GRID_COLS * GRID_CELL_WIDTH

# scoreboard grid
SCOREBOARD_GRID_ROWS = 25
SCOREBOARD_GRID_COLS = 14

# Total dimensions of the window
SCREEN_GRID_ROWS = 25
SCREEN_GRID_COLS = 80

SCREEN_SIZE = (SCREEN_GRID_COLS, SCREEN_GRID_ROWS)

# Total size of the window
WINDOW_HEIGHT = SCREEN_GRID_ROWS * GRID_CELL_HEIGHT
WINDOW_WIDTH = SCREEN_GRID_COLS * GRID_CELL_WIDTH

# colors - colors grabbed from dosbox. pascal uses 16 colors (0-15)

# 0: black
BLACK = Color(0x000000FF)
# 1: blue
BLUE =  Color(0x0000AAFF)
# 2: green
GREEN = Color(0x00AA00FF)
# 3: cyan
CYAN = Color(0x00AAAAFF)
# 4: red
RED = Color(0x9F0000FF)
# 5: magenta
MAGENTA = Color(0xA01FB4FF)
# 6: brown
BROWN = Color(0xAA5500FF)
# 7: lightgray
LIGHTGRAY = Color(0xAAAAAAFF)
# 8: darkgray - NOT USED. color is incorrect but needs a color in case it gets randomly chosen
DARKGRAY = Color(0xAAAAAAFF)
# 9: lightblue
LIGHTBLUE = Color(0x5555FFFF)
# 10: lightgreen
LIGHTGREEN = Color(0x55FF55FF)
# 11: lightcyan
LIGHTCYAN = Color(0x55FFFFFF)
# 12: lightred
LIGHTRED = Color(0xFF5555FF)
# 13: lightmagenta
LIGHTMAGENTA = Color(0xFF55FFFF)
# 14: yellow
YELLOW = Color(0xFFFF55FF)
# 15: white
WHITE = Color(0xFFFFFFFF)

TRANSPARENT = Color(0x00000000)

COLORS = [
    BLACK,
    BLUE,
    GREEN,
    CYAN,
    RED,
    MAGENTA,
    BROWN,
    LIGHTGRAY,
    DARKGRAY,
    LIGHTBLUE,
    LIGHTGREEN,
    LIGHTCYAN,
    LIGHTRED,
    LIGHTMAGENTA,
    YELLOW,
    WHITE,
]

FLASH_EVENT = pygame.event.custom_type()
BLINK_EVENT = pygame.event.custom_type()
