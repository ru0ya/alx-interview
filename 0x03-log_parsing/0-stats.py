#!/usr/bin/python3
"""
interview script
"""
import sys
import re
from collections import Counter
from itertools import groupby


def compute_metrics(lines):
    """Compute metrics from the given lines"""
    total_file_size = 0
    lines_by_status_code = Counter()

    for line in lines:
        match = re.findall(
                r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
                line)
        for status_code, file_size in match:
            total_file_size += int(file_size)
            lines_by_status_code[status_code] += 1

    return total_file_size, lines_by_status_code


def print_results(total_file_size, lines_by_status_code):
    """Print final metrics"""
    print(f"File size: {total_file_size}")

    for code, count in lines_by_status_code.items():
        if count > 0:
            print(f"{code}: {count}")


if __name__ == '__main__':
    lines = sys.stdin.readlines()

    try:
        total_file_size, lines_by_status_code = compute_metrics(lines)
        print_results(total_file_size, lines_by_status_code)
    except KeyboardInterrupt:
        print_results(total_file_size, lines_by_status_code)
        raise
