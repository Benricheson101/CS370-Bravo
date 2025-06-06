from random import randint
from typing import Optional, Tuple, Union
from pygame import Color

from constants import COLORS


ColorValue = Union[Color, int]

def to_color(c: ColorValue, blink: Optional[bool] = False) -> Tuple[Color, bool]:
    """
    Converts `Color | int` to color, blink

    Args:
        c: the color

    Returns:
        color: Color - the pygame Color
        blink: bool - if the color should blink
    """
    if isinstance(c, Color):
        return c, blink or False

    color = c % 16
    blink = bool(c // 16) or blink or False

    return COLORS[color], blink

def new_gem_color() -> Tuple[Color, Color]:
    # TODO: if monochrome mode, these should both be 7
    gem_color = COLORS[8]
    art_color = COLORS[8]

    while gem_color == COLORS[8]:
        gem_color = COLORS[randint(1, 15)]

    while art_color == COLORS[8] or art_color == gem_color:
        art_color = COLORS[randint(1, 15)]

    return gem_color, art_color
