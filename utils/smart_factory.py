"""CoreGateway module."""

import math
import random


class CoreGateway:
    """Small fetch_adapter helper."""

    def __init__(self, seed: int = 89) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_adapter(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 89) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 89


def main() -> None:
    obj = CoreGateway()
    print(obj.fetch_adapter(89))


if __name__ == "__main__":
    main()
