"""
Main module for a simple sketcher.
"""

import curses
import sys

import sketcher.commands as commands
from sketcher.sketcher import Sketcher


def run(stdscr: curses.window) -> None:
    """Starts and runs the sketcher"""
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()  # Use system colours
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)  # Hide the cursor
    stdscr.keypad(True)

    # Setup the sketcher
    sketcher: Sketcher = Sketcher(stdscr)

    # Run commands given on the commandline first
    if len(sys.argv) >= 2:
        cl_cmds: str = sys.argv[1]
        for c in cl_cmds:
            cmd = commands.registry.get(ord(c))
            if cmd:
                cmd(sketcher)
    sketcher.render(True)
    while handle_command(stdscr, sketcher):
        pass


def handle_command(stdscr: curses.window, sketcher: Sketcher) -> bool:
    """Waits for and handles user input"""
    cmd = commands.registry.get(stdscr.getch())
    if cmd and cmd(sketcher) is False:
        return False
    sketcher.render(True)
    return True


@commands.registry.register(commands.command_keys.CMD_QUIT)
def quit_app(_: Sketcher):
    return False


def main() -> None:
    """Main entry point"""
    curses.wrapper(run)


if __name__ == "__main__":
    main()
