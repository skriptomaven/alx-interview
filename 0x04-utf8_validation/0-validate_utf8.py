#!/usr/bin/python3
"""
UTF-8 Validation method
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    n_bytes = 0
    for i in data:
        tmp = 1 << 7
        if not n_bytes:
            while i & tmp:
                n_bytes += 1
                tmp >>= 1
            if not n_bytes:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if i >> 6 != 0b10:
                return False
        n_bytes -= 1
    return n_bytes == 0
