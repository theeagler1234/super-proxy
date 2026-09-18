#!/usr/bin/env python3
"""Display the current CPU and RAM usage of this Linux environment."""

import time
from datetime import datetime


def cpu_times():
    with open("/proc/stat", encoding="utf-8") as proc_stat:
        fields = proc_stat.readline().split()
    return [int(value) for value in fields[1:]]


def cpu_usage(sample_seconds=1.0):
    first = cpu_times()
    time.sleep(sample_seconds)
    second = cpu_times()

    total_delta = sum(second) - sum(first)
    idle_delta = (second[3] + second[4]) - (first[3] + first[4])
    if total_delta <= 0:
        return 0.0
    return (1 - idle_delta / total_delta) * 100


def memory_usage():
    memory = {}
    with open("/proc/meminfo", encoding="utf-8") as meminfo:
        for line in meminfo:
            key, value = line.split(":", 1)
            memory[key] = int(value.split()[0])

    total = memory["MemTotal"]
    available = memory["MemAvailable"]
    used = total - available
    return used, total, (used / total) * 100


def main():
    try:
        while True:
            cpu_percent = cpu_usage()
            used_kib, total_kib, memory_percent = memory_usage()
            mib = 1024

            print("\033[2J\033[H", end="")
            print(f"Codespace resource usage ({datetime.now():%Y-%m-%d %H:%M:%S})")
            print(f"CPU usage: {cpu_percent:.1f}%")
            print(
                "RAM usage: "
                f"{used_kib / mib:.0f} MiB / {total_kib / mib:.0f} MiB "
                f"({memory_percent:.1f}%)"
            )
            print("\nPress Ctrl+C to exit.", flush=True)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()
