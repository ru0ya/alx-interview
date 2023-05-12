#!/usr/bin/python3
"""
interview script
"""
import sys
from collections import defaultdict
import re


def compute_metrics(lines):
    """Compute metrics from the given lines"""
    total_file_size = 0
    lines_by_status_code = defaultdict(int)
    lines_processed = 0

    for line in lines:
        match = re.match(
                r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
                line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            total_file_size += file_size
            lines_by_status_code[status_code] += 1
            lines_processed += 1

        if lines_processed % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in status_codes:
                if lines_by_status_code[code] > 0:
                    print(f"{code}: {lines_by_status_code[code]}")

    return total_file_size, lines_by_status_code


def print_results(total_file_size, lines_by_status_code):
    """Print final metrics"""
    print(f"File size: {total_file_size}")
    for code in status_codes:
        if lines_by_status_code[code] > 0:
            print(f"{code}: {lines_by_status_code[code]}")


if __name__ == '__main__':
    lines = sys.stdin.readlines()

    try:
        total_file_size, lines_by_status_code = compute_metrics(lines)
        print_results(total_file_size, lines_by_status_code)
    except KeyboardInterrupt:
        print_results(total_file_size, lines_by_status_code)
        raise
