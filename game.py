import queue
import pygame
from state import State


class Game:
    def __init__(self, window_title: str, resolution: tuple[int, int], tick_rate: int, first_state: State):
        self.display = None
        self._window_title = window_title
        self._resolution = resolution
        self.current_state = first_state
        self._state_stack = queue.Queue()
        self._running = True
        self._clock = pygame.time.Clock()
        self._tick_rate = tick_rate

    def run(self):
        pygame.display.set_caption(self._window_title)
        self.display = pygame.display.set_mode(self._resolution)
        clock = pygame.time.Clock()

        while self._running:
            dt = clock.tick(self.tick_rate)
            self.current_state.update(dt)
            self.current_state.draw()
            if self.current_state.finished:
                new_state = self.current_state.end()
                if new_state:
                    self.current_state = new_state
                else:
                    self.current_state = self._state_stack.get()
