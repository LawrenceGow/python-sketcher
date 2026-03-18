"""
Module for the command registry.
"""

from typing import Callable

from sketcher.sketcher import Sketcher

CommandHandler = Callable[[Sketcher], bool | None]


class CommandRegistry:

    def __init__(self):
        self._commands: dict[int, CommandHandler] = {}

    def register(self, key: int):

        def decorator(func: CommandHandler):
            if key in self._commands:
                raise ValueError(
                    "Attempted to register a second command with the same" +
                    f"key '{chr(key)}'.")
            self._commands[key] = func
            return func

        return decorator

    def get(self, key: int) -> CommandHandler | None:
        return self._commands.get(key)


registry = CommandRegistry()
