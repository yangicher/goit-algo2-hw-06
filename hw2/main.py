from log_loader import load_ips_from_log
from exact_counter import exact_unique_count
from hll_counter import hll_unique_count
from benchmark import measure_time


LOG_FILE = "lms-stage-access.log"


def main():
    ips = list(load_ips_from_log(LOG_FILE))

    exact_result, exact_time = measure_time(exact_unique_count, ips)
    hll_result, hll_time = measure_time(lambda data: hll_unique_count(data, p=12), ips)

    print("\nРезультати порівняння:")
    print(f"{'':30}Точний підрахунок     HyperLogLog")
    print(f"{'Унікальні елементи':30}{exact_result:>10.1f}{hll_result:>15.1f}")
    print(f"{'Час виконання (сек.)':30}{exact_time:>10.2f}{hll_time:>15.2f}")


if __name__ == "__main__":
    main()
