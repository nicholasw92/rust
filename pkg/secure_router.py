"""AsyncManager module."""

import math
import random


class AsyncManager:
    """Small flush_scheduler helper."""

    def __init__(self, seed: int = 67) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_scheduler(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 67) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 67


def main() -> None:
    obj = AsyncManager()
    print(obj.flush_scheduler(67))


if __name__ == "__main__":
    main()
