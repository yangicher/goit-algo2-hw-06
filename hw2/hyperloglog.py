import hashlib
import math


class HyperLogLog:
    def __init__(self, p=10):
        if not (4 <= p <= 16):
            raise ValueError("p must be in range [4, 16]")

        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m

        if self.m == 16:
            self.alpha = 0.673
        elif self.m == 32:
            self.alpha = 0.697
        elif self.m == 64:
            self.alpha = 0.709
        else:
            self.alpha = 0.7213 / (1 + 1.079 / self.m)

    def _hash(self, value: str) -> int:
        return int(hashlib.sha1(value.encode("utf-8")).hexdigest(), 16)

    def add(self, value: str):
        x = self._hash(value)

        idx = x & (self.m - 1)
        w = x >> self.p

        rho = self._leading_zeros(w) + 1
        self.registers[idx] = max(self.registers[idx], rho)

    @staticmethod
    def _leading_zeros(x: int) -> int:
        if x == 0:
            return 64
        return (x.bit_length() - 1) ^ 63

    def count(self) -> float:
        indicator = sum(2**-r for r in self.registers)
        E = self.alpha * self.m * self.m / indicator

        if E <= 2.5 * self.m:
            V = self.registers.count(0)
            if V != 0:
                return self.m * math.log(self.m / V)

        return E
