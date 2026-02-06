from typing import Iterator


class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")
        if not isinstance(num_hashes, int) or num_hashes <= 0:
            raise ValueError("num_hashes must be a positive integer")

        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bytearray(size)

    def _hashes(self, item: str) -> Iterator[int]:
        for i in range(self.num_hashes):
            yield hash(f"{item}_{i}") % self.size

    def add(self, item: str) -> None:
        if not isinstance(item, str) or item == "":
            return

        for index in self._hashes(item):
            self.bit_array[index] = 1

    def contains(self, item: str) -> bool:
        if not isinstance(item, str) or item == "":
            return False

        return all(self.bit_array[index] for index in self._hashes(item))
