"""RemoteGateway module."""

import math
import random


class RemoteGateway:
    """Small compute_handler helper."""

    def __init__(self, seed: int = 69) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_handler(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 69) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 69


def main() -> None:
    obj = RemoteGateway()
    print(obj.compute_handler(69))


if __name__ == "__main__":
    main()
