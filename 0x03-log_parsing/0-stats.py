#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys
from collections import defaultdict


def compute_metrics(lines):
    """Compute metrics from the given lines"""
    status_codes = defaultdict(int)
    file_size = 0

    for line in lines:
        data = line.split()
        try:
            status_code = data[-2]
            status_codes[status_code] += 1
            file_size += int(data[-1])
        except (IndexError, ValueError):
            pass

    return status_codes, file_size


def print_results(status_codes, file_size):
    """Print statistics"""
    print("File size:", file_size)
    for status_code, times in sorted(status_codes.items()):
        if times:
            print(status_code + ":", times)


if __name__ == '__main__':
    lines = sys.stdin.readlines()

    try:
        while lines:
            chunk = lines[:10]
            lines = lines[10:]
            status_codes, file_size = compute_metrics(chunk)
            print_results(status_codes, file_size)
    except KeyboardInterrupt:
        print_results(status_codes, file_size)
        raise
