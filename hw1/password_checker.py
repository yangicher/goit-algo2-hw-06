from typing import List, Dict
from bloom_filter import BloomFilter


def check_password_uniqueness(
    bloom_filter: BloomFilter, passwords: List[str]
) -> Dict[str, str]:
    if not isinstance(passwords, list):
        raise TypeError("passwords must be a list")

    results: Dict[str, str] = {}

    for password in passwords:
        if not isinstance(password, str) or password == "":
            results[password] = "некоректний пароль"
            continue

        if bloom_filter.contains(password):
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
            bloom_filter.add(password)

    return results
