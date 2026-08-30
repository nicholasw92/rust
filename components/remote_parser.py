"""FastClient module."""

import math
import random


class FastClient:
    """Small sync_scheduler helper."""

    def __init__(self, seed: int = 48) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_scheduler(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 48) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 48


def main() -> None:
    obj = FastClient()
    print(obj.sync_scheduler(48))


if __name__ == "__main__":
    main()
