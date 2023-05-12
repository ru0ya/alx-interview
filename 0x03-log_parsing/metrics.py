#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys


def print_results(status_codes, file_size):
    """Print statistics"""
    print("File size: {}".format(file_size))
    for status_code, times in sorted(status_codes.items()):
        if times:
            print("{}: {}".format(status_code, times))


def compute_metrics(lines):
    """Compute metrics from the given lines"""
    status_codes = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0
                    }
    file_size = 0

    for line in lines:
        data = line.split()
        try:
            status_code = data[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            file_size += int(data[-1])
        except IndexError:
            pass
        except ValueError:
            pass

    return status_codes, file_size


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    status_codes, file_size = compute_metrics(lines)
    print_results(status_codes, file_size)

