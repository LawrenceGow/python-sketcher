"""
Module for a player entity.
"""

from .entity import Entity


class Player(Entity):

    def __init__(self, x: int, y: int, max_x: int, max_y: int) -> None:
        super().__init__(x, y, max_x, max_y)
        self.hidden = False

    @property
    def glyph(self) -> str:
        return self._glyph

    @glyph.setter
    def glyph(self, value: str) -> None:
        self._glyph = value

    def move_x(self, increase: bool) -> bool:
        old_x = self.x
        self.x += 1 if increase else -1
        return old_x != self.x

    def move_y(self, increase: bool) -> bool:
        old_y = self.y
        self.y += 1 if increase else -1
        return old_y != self.y
