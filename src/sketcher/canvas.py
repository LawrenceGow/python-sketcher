"""
Module for the canvas class.
"""

import curses
import math
from contextlib import suppress

from sketcher.entities.tile import DEFAULT_TILE_GLYPH

from .entities import Tile


class Canvas:

    def __init__(self, stdscr: curses.window) -> None:
        self._stdscr = stdscr
        self._max_y, self._max_x = stdscr.getmaxyx()
        self._tile_grid: list[list[Tile | None]] = [[
            None for _ in range((self._max_x) // 2)
        ] for _ in range(self._max_y - 1)]
        self._trail_mode: bool = False
        self._line_start: tuple[int, int] | None = None

    def _remv_entity(self, tile: Tile) -> None:
        """Clears the screen at the given Tile's position"""
        with suppress(curses.error):
            self._stdscr.addstr(tile.y, tile.x * 2, "  ")

    def _draw_entity(self, tile: Tile) -> None:
        """Draws the given Tile to the screen"""
        with suppress(curses.error):
            self._stdscr.addstr(tile.y, tile.x * 2, str(tile),
                                curses.color_pair(tile.color))

    def render(self, render_mode: bool) -> None:
        """Renders to the canvas"""
        [self._draw_entity(t) for row in self._tile_grid for t in row if t]
        if render_mode and self._trail_mode:
            self._stdscr.addstr(self._max_y - 1, 0, "TRAIL")

    def create_tile(self, x: int, y: int, color: int) -> Tile:
        return Tile(x, y, DEFAULT_TILE_GLYPH, color)

    def _fill_check(self, x: int, y: int, initial_color: int,
                    p: set[tuple[int, int]]) -> bool:
        """Checks if the specified location is valid for filling"""
        if (x, y) in p \
                or 0 > y or y >= len(self._tile_grid) \
                or 0 > x or x >= len(self._tile_grid[0]):
            return False
        t: Tile | None = self._tile_grid[y][x]
        if not t and initial_color > -1 \
                or t and t.color != initial_color:
            return False
        return True

    def _draw_line(self, x: int, y: int, color: int) -> None:
        """Draws a straight line between _line_start and the given position"""
        if not self._line_start:
            self._line_start = (x, y)
            return
        if (x, y) == self._line_start:
            return
        for yy in range(min(y, self._line_start[1]),
                        max(y, self._line_start[1]) + 1):
            for xx in range(min(x, self._line_start[0]),
                            max(x, self._line_start[0]) + 1):
                numerator = math.fabs((y - self._line_start[1]) * xx -
                                      (x - self._line_start[0]) * yy +
                                      x * self._line_start[1] -
                                      y * self._line_start[0])
                denomintator = math.sqrt((y - self._line_start[1])**2 +
                                         (x - self._line_start[0])**2)
                distance = numerator / denomintator
                if distance < 0.5:
                    self._tile_grid[yy][xx] = self.create_tile(xx, yy, color)

    def clear_canvas(self) -> None:
        """Clears the canvas of all placed tiles"""
        for y in range(len(self._tile_grid)):
            self._tile_grid[y] = [None for _ in self._tile_grid[y]]
        self._stdscr.clear()

    def save_tiles(self, filename: str | None = None) -> None:
        """Saves the placed tiles to the specified file"""
        if not filename:
            filename = self._get_filename("SAVE FILE", True)
        if not filename:
            return
        tiles_to_save: list[Tile] = [
            t for row in self._tile_grid for t in row if t
        ]
        Tile.save_tiles(filename, tiles_to_save)

    def load_tiles(self, filename: str | None = None) -> None:
        """Loads placed tiles from the specified file"""
        if not filename:
            filename = self._get_filename("LOAD FILE", True)
        if not filename:
            return
        with suppress(FileNotFoundError):
            loaded_tiles: list[Tile] = Tile.load_tiles(filename)
            for t in loaded_tiles:
                with suppress(IndexError):
                    self._tile_grid[t.y][t.x] = t
        self._stdscr.clear()

    def _get_filename(self, prefix: str, force_ext: bool) -> str | None:
        """Prompts the user to input a filename and returns the result"""
        self._stdscr.addstr(self._max_y - 1, 0, f"{prefix}:")
        self.render(False)
        filename = ""
        while True:
            c = self._stdscr.getch()
            if c == curses.KEY_BACKSPACE:
                filename = filename[:-1]
            elif c == 27:  # Press ESC to cancel the input
                self._stdscr.addstr(self._max_y - 1, 0,
                                    " " * (self._max_x - 1))
                self.render(True)
                return None
            else:
                c_str = chr(c)
                if c_str == "\n":
                    break
                filename += c_str
            self._stdscr.addstr(self._max_y - 1, 0, " " * (self._max_x - 1))
            self._stdscr.addstr(self._max_y - 1, 0, f"{prefix}: {filename}")
            self.render(False)
        self._stdscr.addstr(self._max_y - 1, 0, " " * (self._max_x - 1))
        self.render(True)
        if force_ext and filename.lower()[-5:] != ".json":
            filename += ".json"
        return filename
