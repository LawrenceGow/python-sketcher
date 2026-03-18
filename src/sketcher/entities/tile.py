"""
Module for tiles.
"""

import json

DEFAULT_TILE_GLYPH = "██"


class Tile:

    def __init__(self, x: int, y: int, glyph: str, color: int) -> None:
        self._x = x
        self._y = y
        self._glyph = glyph
        self._color = color

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def color(self) -> int:
        return self._color

    @color.setter
    def color(self, value: int) -> None:
        self._color = value % 16

    @property
    def glyph(self) -> str:
        return self._glyph

    def __str__(self) -> str:
        return self.glyph

    @staticmethod
    def save_tiles(filename: str, placed_tiles: list[Tile]) -> None:
        with open(filename, "w") as f:
            f.write(json.dumps(placed_tiles, cls=TileEncoder))

    @staticmethod
    def load_tiles(filename: str) -> list[Tile]:
        loaded_tiles: list[Tile] = []
        with open(filename, "r") as f:
            json_str = f.read()
            for tile_data in json.loads(json_str):
                loaded_tiles.append(
                    Tile(
                        tile_data["_x"],
                        tile_data["_y"],
                        tile_data["_glyph"],
                        tile_data["_color"],
                    ))
        return loaded_tiles


class TileEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Tile):
            return o.__dict__
        return super().default(o)
