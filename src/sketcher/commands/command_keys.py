"""
Module for all supported commands.
"""

import curses

CMD_MV_L: int = ord("a")
CMD_MV_U: int = ord("w")
CMD_MV_R: int = ord("d")
CMD_MV_D: int = ord("s")

CMD_SH_L: int = ord("A")
CMD_SH_U: int = ord("W")
CMD_SH_R: int = ord("D")
CMD_SH_D: int = ord("S")

CMD_CLEAR: int = curses.KEY_BACKSPACE
CMD_PLACE: int = ord("#")
CMD_FILL: int = ord("~")
CMD_TOGGLE_TRAIL: int = ord("t")
CMD_TOGGLE_PALETTE: int = ord("C")
CMD_HIDE: int = ord("h")
CMD_NEW_PAGE: int = ord("N")
CMD_LINE: int = ord("l")

CMD_SAVE: int = ord("}")
CMD_QSAVE: int = ord("]")
CMD_LOAD: int = ord("{")
CMD_QLOAD: int = ord("[")
CMD_QUIT: int = ord("Q")
CMD_SAVE_QUIT: int = ord("X")
