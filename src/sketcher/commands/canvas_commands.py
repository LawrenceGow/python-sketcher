"""
Module to define our built-in canvas commands.
"""

from functools import partial

from sketcher.constants import AVAILABLE_COLORS
from sketcher.sketcher import Sketcher

from .command_keys import (CMD_CLEAR, CMD_FILL, CMD_HIDE, CMD_LINE,
                           CMD_NEW_PAGE, CMD_PLACE, CMD_TOGGLE_PALETTE,
                           CMD_TOGGLE_TRAIL)
from .command_registry import registry


@registry.register(CMD_CLEAR)
def clear_tile(sketcher: Sketcher) -> None:
    sketcher.clear_tile_at_cursor()


@registry.register(CMD_PLACE)
def place_tile(sketcher: Sketcher) -> None:
    sketcher.place_tile()


@registry.register(CMD_FILL)
def fill_area(sketcher: Sketcher) -> None:
    sketcher.fill_area()


@registry.register(CMD_TOGGLE_PALETTE)
def toggle_color_palette(sketcher: Sketcher) -> None:
    sketcher.change_color()


def change_color(sketcher: Sketcher, new_color: int) -> None:
    sketcher.change_color(new_color)


for key in AVAILABLE_COLORS:
    registry.register(key)(partial(change_color, new_color=key))


@registry.register(CMD_TOGGLE_TRAIL)
def toggle_trail(sketcher: Sketcher) -> None:
    sketcher.toggle_trail_mode()


@registry.register(CMD_NEW_PAGE)
def new_page(sketcher: Sketcher) -> None:
    sketcher.clear_canvas()


@registry.register(CMD_HIDE)
def toggle_cursor(sketcher: Sketcher) -> None:
    sketcher.toggle_cursor()


@registry.register(CMD_LINE)
def draw_line(sketcher: Sketcher) -> None:
    sketcher.draw_line()
