#!/usr/bin/python3
"""
Takes an input format <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
 if format is same: Returns total size of file size
 With every 10 lines or key interrupt
 """


import sys
import re
from collections import defaultdict


input_format = r'^(\d+\.\d+\.\d+\.\d+) -\[(\d{4}-\d{2}-\d{2})\]"GET\/projects\/(\d+) HTTP\/\d\.\d" (\d{3}) (\d+)$'
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0
total_file_size = 0
status_code_count = defaultdict(int)


try:
    for line in sys.stdin:
        similar = re.match(input_format, line.strip())
        if similar:
            file_size = int(similar.group(5))
            total_file_size += file_size

            status_code = similar.group(4)
            status_code_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print('File size:', total_file_size)

                for code in status_codes:
                    if status_code_count[code] > 0:
                        print(f'{code}: {status_code_count[code]}')

except KeyboardInterrupt:
    print('File size:', total_file_size)

    for code in status_codes:
        if status_code_count[code] > 0:
            print(f'{code}: {status_code_count[code]}')
