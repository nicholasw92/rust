"""AtomicController module."""

import math
import random


class AtomicController:
    """Small build_scheduler helper."""

    def __init__(self, seed: int = 53) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_scheduler(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 53) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 53


def main() -> None:
    obj = AtomicController()
    print(obj.build_scheduler(53))


if __name__ == "__main__":
    main()
