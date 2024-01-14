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

def is_row_safe(board, row, col, n):
    """ Check if the queen is in the same row.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def nqueens_solution(board, col, n):
    if col == n:
        print_sol(board, n)
        return

    for i in range(n):
        if is_row_safe(board, i, col, n): 
            board[i][col] = 1
            nqueens_solution(board, col + 1, n)

            board[i][col] = 0

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]

    nqueens_solution(board, 0, n)

def print_sol(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
