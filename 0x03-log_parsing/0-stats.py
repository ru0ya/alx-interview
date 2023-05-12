#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re
from collections import defaultdict


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    pattern = re.compile(
        r'\s*(?P<ip>\S+)\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]'
        r'\s*"(?P<request>[^"]*)"\s*(?P<status_code>\S+)\s*(?P<file_size>\d+)'
    )
    match = pattern.match(input_line)
    if match:
        info = {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
        return info
    return None


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size:', total_file_size)
    for status_code, num in sorted(status_codes_stats.items()):
        if num > 0:
            print(status_code + ':', num)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current status code statistics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    if line_info:
        status_code = line_info['status_code']
        status_codes_stats[status_code] += 1
        total_file_size += line_info['file_size']
    return total_file_size


def run():
    '''Starts the log parser.
    '''
    total_file_size = 0
    status_codes_stats = defaultdict(int)
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats
            )
            if len(status_codes_stats) % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
