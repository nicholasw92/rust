"""AsyncGateway module."""

import math
import random


class AsyncGateway:
    """Small collect_context helper."""

    def __init__(self, seed: int = 65) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_context(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 65) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 65


def main() -> None:
    obj = AsyncGateway()
    print(obj.collect_context(65))


if __name__ == "__main__":
    main()
