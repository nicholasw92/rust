"""HybridDispatcher module."""

import math
import random


class HybridDispatcher:
    """Small render_controller helper."""

    def __init__(self, seed: int = 58) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_controller(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 58) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 58


def main() -> None:
    obj = HybridDispatcher()
    print(obj.render_controller(58))


if __name__ == "__main__":
    main()
