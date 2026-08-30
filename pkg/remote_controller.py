"""LiteScheduler module."""

import math
import random


class LiteScheduler:
    """Small run_handler helper."""

    def __init__(self, seed: int = 18) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_handler(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 18) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 18


def main() -> None:
    obj = LiteScheduler()
    print(obj.run_handler(18))


if __name__ == "__main__":
    main()
