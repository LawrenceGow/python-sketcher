"""
Module for entity logic.
"""

from .tile import Tile


class Entity(Tile):

    def __init__(self, x: int, y: int, max_x: int, max_y: int) -> None:
        super().__init__(x, y, "?", 0)
        self._max_x = max_x
        self._max_y = max_y

    @property
    def x(self) -> int:
        return super().x

    @x.setter
    def x(self, value: int) -> None:
        if 0 <= value < self._max_x:
            self._x = value

    @property
    def y(self) -> int:
        return super().y

    @y.setter
    def y(self, value: int) -> None:
        if 0 <= value < self._max_y:
            self._y = value
