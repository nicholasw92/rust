"""AtomicDispatcher module."""

import math
import random


class AtomicDispatcher:
    """Small dispatch_registry helper."""

    def __init__(self, seed: int = 35) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_registry(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 35) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 35


def main() -> None:
    obj = AtomicDispatcher()
    print(obj.dispatch_registry(35))


if __name__ == "__main__":
    main()
