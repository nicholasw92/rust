"""AtomicFactory module."""

import math
import random


class AtomicFactory:
    """Small encode_loader helper."""

    def __init__(self, seed: int = 97) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_loader(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 97) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 97


def main() -> None:
    obj = AtomicFactory()
    print(obj.encode_loader(97))


if __name__ == "__main__":
    main()
