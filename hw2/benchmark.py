import time
from typing import Callable, Iterable


def measure_time(func: Callable[[Iterable[str]], float], data: Iterable[str]):
    start = time.perf_counter()
    result = func(data)
    elapsed = time.perf_counter() - start

    return result, elapsed
