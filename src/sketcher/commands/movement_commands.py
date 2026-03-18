"""
Module to define our built-in movement commands.
"""

from functools import partial

from sketcher.sketcher import Sketcher

from .command_keys import (CMD_MV_D, CMD_MV_L, CMD_MV_R, CMD_MV_U, CMD_SH_D,
                           CMD_SH_L, CMD_SH_R, CMD_SH_U)
from .command_registry import registry


def move(sketcher: Sketcher, dx: int, dy: int, shift: bool) -> None:
    sketcher.move_cursor(dx, dy, shift)


MOVEMENTS = {
    CMD_MV_L: (-1, 0, False),
    CMD_MV_R: (1, 0, False),
    CMD_MV_U: (0, -1, False),
    CMD_MV_D: (0, 1, False),
    CMD_SH_L: (-1, 0, True),
    CMD_SH_R: (1, 0, True),
    CMD_SH_U: (0, -1, True),
    CMD_SH_D: (0, 1, True),
}

for key, (dx, dy, shift) in MOVEMENTS.items():
    registry.register(key)(partial(move, dx=dx, dy=dy, shift=shift))
