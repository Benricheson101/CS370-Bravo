# TODO: try to make this scale automatically based on display size
from pygame import Color


SCALE = 2

# The size of a single grid cell
GRID_CELL_HEIGHT = 16 * SCALE
GRID_CELL_WIDTH = 9 * SCALE

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

# Total size of the window
WINDOW_HEIGHT = SCREEN_GRID_ROWS * GRID_CELL_HEIGHT
WINDOW_WIDTH = SCREEN_GRID_COLS * GRID_CELL_WIDTH

# colors

# FIXME: these are temporary colors, need to look up actual dos colors
RED = Color(0xFF0000FF)
GREEN = Color(0x00FF00FF)
BLUE = Color(0x0000FFFF)
CYAN = Color(0x00FFFFFF)
GRAY = Color(0x808080FF)
BLACK = Color(0x000000FF)
WHITE = Color(0x000000FF)
YELLOW = Color(0xFFFF00FF)
ORANGE = Color(0xAA5500FF)
PURPLE = Color(0x800080)
