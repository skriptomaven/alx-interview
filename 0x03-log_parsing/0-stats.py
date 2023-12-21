#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys


if __name__ == "__main__":
    """ Reads stdin line by line."""
    file_size = 0
    count = 0
    status_codes = ["200", "301", "400", "403", "404", "405", "500"]
    status = {i: 0 for i in status_codes}

    def print_status(status: dict, fileSize: int) -> None:
        print("File size: {:d}".format(file_size))
        for i, j in sorted(status.items()):
            if j:
                print("{}: {}".format(i, j))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in status:
                    status[status_code] += 1
            except BaseException:
                pass
            try:
                fileSize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_status(status, file_size)
        print_status(status, file_size)
    except KeyboardInterrupt:
        print_status(status, file_size)
        raise
