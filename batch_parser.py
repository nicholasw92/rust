"""AsyncResolver module."""

import math
import random


class AsyncResolver:
    """Small load_client helper."""

    def __init__(self, seed: int = 50) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_client(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 50) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 50


def main() -> None:
    obj = AsyncResolver()
    print(obj.load_client(50))


if __name__ == "__main__":
    main()
