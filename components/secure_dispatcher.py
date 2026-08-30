"""AsyncCache module."""

import math
import random


class AsyncCache:
    """Small parse_monitor helper."""

    def __init__(self, seed: int = 64) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_monitor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 64) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 64


def main() -> None:
    obj = AsyncCache()
    print(obj.parse_monitor(64))


if __name__ == "__main__":
    main()
