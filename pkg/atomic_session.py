"""SecureParser module."""

import math
import random


class SecureParser:
    """Small resolve_scheduler helper."""

    def __init__(self, seed: int = 90) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_scheduler(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 90) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 90


def main() -> None:
    obj = SecureParser()
    print(obj.resolve_scheduler(90))


if __name__ == "__main__":
    main()
