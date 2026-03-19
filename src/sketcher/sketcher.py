"""
Module for the sketcher.
"""

import curses
import queue

from .canvas import Canvas
from .constants import AVAILABLE_COLORS
from .entities import DEFAULT_TILE_GLYPH, Player, Tile


class Sketcher(Canvas):

    def __init__(self, stdscr: curses.window) -> None:
        super().__init__(stdscr)
        grid_width: int = len(self._tile_grid[0])
        self._player: Player = Player(grid_width // 2, self._max_y // 2,
                                      grid_width, self._max_y - 1)
        self._player.glyph = "▓▓"  # █▓▒░

    def move_cursor(self, x: int, y: int, shift: bool) -> None:
        """Moves the cursor in the specified direction (x XOR y)"""
        self._remv_entity(self._player)
        if x:
            while self._player.move_x(x > 0):
                if self._trail_mode:
                    self.place_tile()
                if not shift:
                    break
        elif y:
            while self._player.move_y(y > 0):
                if self._trail_mode:
                    self.place_tile()
                if not shift:
                    break

    def render(self, render_mode: bool) -> None:
        """Renders to the canvas"""
        super().render(render_mode)
        if not self._player.hidden:
            self._draw_entity(self._player)
        self._stdscr.refresh()

    def change_color(self, new_color: int | None = None) -> None:
        """Prompts the user for what colour they wish to switch to"""

        def set_color(c: int) -> bool:
            for i in range(len(AVAILABLE_COLORS)):
                if c == AVAILABLE_COLORS[i]:
                    self._player.color = i
                    return True
            else:
                return False

        if new_color and set_color(new_color):
            return
        # Display a palette of colours to choose from
        for i in range(16):
            self._stdscr.addstr(i, 0, DEFAULT_TILE_GLYPH, curses.color_pair(i))
            self._stdscr.addstr(i, 3, chr(AVAILABLE_COLORS[i]),
                                curses.color_pair(i))
        self._stdscr.refresh()
        key = self._stdscr.getch()
        if not set_color(key):
            self._player.color = 0
        # Erase the palette of colours
        for i in range(16):
            self._stdscr.addstr(i, 0, "    ")
        if self._trail_mode:
            self.place_tile()

    def toggle_trail_mode(self) -> None:
        """Toggles the trail mode on/off"""
        self._trail_mode = not self._trail_mode
        if self._trail_mode:
            self.place_tile()
            return
        self._stdscr.addstr(self._max_y - 1, 0, "     ")

    def toggle_cursor(self) -> None:
        """Toggles the cursor on/off"""
        self._player.hidden = not self._player.hidden
        if self._player.hidden:
            self._remv_entity(self._player)

    def create_tile_at_cursor(self) -> Tile:
        return self.create_tile(self._player.x, self._player.y,
                                self._player.color)

    def place_tile(self) -> None:
        """Places a Tile at the cursor's position"""
        if self._player.hidden:
            return
        self._line_start = (self._player.x, self._player.y)
        t: Tile | None = self._tile_grid[self._player.y][self._player.x]
        if t:
            t.color = self._player.color
            return
        self._tile_grid[self._player.y][
            self._player.x] = self.create_tile_at_cursor()

    def fill_area(self) -> None:
        """Fills an area with no/matching tiles"""
        if self._player.hidden:
            return
        p = set()
        q = queue.LifoQueue()
        initial_tile: Tile | None = self._tile_grid[self._player.y][
            self._player.x]
        initial_color = initial_tile.color if initial_tile else -1
        q.put((self._player.x, self._player.y))
        while not q.empty():
            x, y = q.get()
            self._tile_grid[y][x] = self.create_tile(x, y, self._player.color)
            p.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if self._fill_check(x + dx, y + dy, initial_color, p):
                    q.put((x + dx, y + dy))

    def draw_line(self) -> None:
        """Draws a straight line between _line_start and cursor's position"""
        if self._player.hidden:
            return
        self._draw_line(self._player.x, self._player.y, self._player.color)
        self._line_start = (self._player.x, self._player.y)

    def clear_tile_at_cursor(self) -> None:
        """Removes any Tiles at the cursor's position"""
        if self._player.hidden:
            return
        self._tile_grid[self._player.y][self._player.x] = None
