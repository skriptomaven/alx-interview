#!/usr/bin/python3
""" Solution to N queens problem.
"""
import sys


if len(sys.argv) != 2:
    """ If user calls the program with the wrong number
    of arguments.
    """
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
