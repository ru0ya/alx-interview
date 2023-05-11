#!/usr/bin/python3
"""
Takes an input format <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
 if format is same: Returns total size of file size
 With every 10 lines or key interrupt
 """


import sys
import re


n = input()

input_format = r'^(\d+\.\d+\.\d+\.\d+) -\[(\d{4}-\d{2}-\d{2})\]
"GET\/projects\/(\d+) HTTP\/\d\.\d" (\d{3} (\d+)$'

line_count = 0
total_file_size = 0


try:
    for line in sys.stdin:
        similar = re.match(input_format, line.strip())
        if match:
            file_size = int(match.group(5))
            total_file_size += file_size

            line_count += 1
            print(f'{status_code}: {number}')

            if line_count % 10 == 0:
                print(f'File size: {total_file_size}')
except KeyboardInterrupt:
    print(f'File size: {total_file_size}')
