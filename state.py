from __future__ import annotations

from game import Game
from abc import abstractmethod


class State:
    def __init__(self, game: Game, preserved=None):
        if preserved is None:
            preserved = {}

        self.preserved = preserved
        self.finished = False
        self._game = game

    @abstractmethod
    def begin(self) -> None:
        pass

    @abstractmethod
    def update(self, dt: int) -> None:
        pass

    @abstractmethod
    def end(self) -> State | None:
        pass
