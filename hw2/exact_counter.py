from typing import Iterable


def exact_unique_count(ips: Iterable[str]) -> int:
    unique_ips = set()

    for ip in ips:
        unique_ips.add(ip)

    return len(unique_ips)
