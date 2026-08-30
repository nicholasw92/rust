"""BatchProvider module."""

import math
import random


class BatchProvider:
    """Small encode_controller helper."""

    def __init__(self, seed: int = 59) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_controller(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 59) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 59


def main() -> None:
    obj = BatchProvider()
    print(obj.encode_controller(59))


if __name__ == "__main__":
    main()
