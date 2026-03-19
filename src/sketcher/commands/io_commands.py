"""
Module to define our built-in IO commands.
"""

from sketcher.sketcher import Sketcher

from .command_keys import (CMD_LOAD, CMD_QLOAD, CMD_QSAVE, CMD_SAVE,
                           CMD_SAVE_QUIT)
from .command_registry import registry

SKETCH_FILENAME = "~/quick_sketch.json"


@registry.register(CMD_SAVE)
def save(sketcher: Sketcher) -> None:
    sketcher.save_tiles()


@registry.register(CMD_QSAVE)
def quick_save(sketcher: Sketcher) -> None:
    sketcher.save_tiles(SKETCH_FILENAME)


@registry.register(CMD_LOAD)
def load(sketcher: Sketcher) -> None:
    sketcher.load_tiles()


@registry.register(CMD_QLOAD)
def quick_load(sketcher: Sketcher) -> None:
    sketcher.load_tiles(SKETCH_FILENAME)


@registry.register(CMD_SAVE_QUIT)
def quit_app(sketcher: Sketcher) -> bool:
    quick_save(sketcher)
    return False
