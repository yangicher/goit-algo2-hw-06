from hyperloglog import HyperLogLog


def hll_unique_count(data, p=10):
    hll = HyperLogLog(p=p)
    for ip in data:
        hll.add(ip)
    return hll.count()
