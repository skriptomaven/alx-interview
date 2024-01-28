#!/usr/bin/python3
'''
0. Rotate 2D Matrix module.
'''


def rotate_2d_matrix(matrix) -> None:
    '''
    Rotates an n by n 2D matrix 90 degress clockwise.
    '''
    n = len(matrix)
    for i in range(n // 2):
        first, last, offset = i, n - 1 - i, 0
        for j in range(first, last):
            top = matrix[first][1]
            matrix[first][j] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[j][last]
            matrix[j][last] = top
            offset += 1
