#!/usr/bin/python3
"""
Minimum operations module
"""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to result
    in exactly n H characters in the file. Returns an integer. If
    n is impossible to achieve, return 0.
    """
    tmp = "H"
    temp = "H"
    ops = 0
    while (len(temp) < n):
        if n % len(temp) == 0:
            ops += 2
            tmp = temp
            temp += temp
        else:
            ops += 1
            temp += tmp
    if len(temp) != n:
        return 0
    return ops
