import json
from typing import Iterator


def load_ips_from_log(filepath: str) -> Iterator[str]:
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            try:
                record = json.loads(line.strip())
                ip = record.get("remote_addr")

                if isinstance(ip, str) and ip:
                    yield ip

            except json.JSONDecodeError:
                continue
