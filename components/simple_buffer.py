"""SecureFactory module."""

import math
import random


class SecureFactory:
    """Small dispatch_buffer helper."""

    def __init__(self, seed: int = 94) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_buffer(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 94) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 94


def main() -> None:
    obj = SecureFactory()
    print(obj.dispatch_buffer(94))


if __name__ == "__main__":
    main()
