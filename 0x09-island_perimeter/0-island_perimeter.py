#!/usr/bin/python3
'''
Island perimeter module.
'''


def island_perimeter(grid):
    '''
    Returns the perimeter of the island described in grid.
    '''
    perimeter = 0
    for i, j in enumerate(grid):
        for k, cell in enumerate(j):
            if cell == 1:
                if i == 0 or grid[i - 1][k] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][k] == 0:
                    perimeter += 1
                if k == 0 or grid[i][k - 1] == 0:
                    perimeter += 1
                if k == len(j) - 1 or grid[i][k + 1] == 0:
                    perimeter += 1
    return perimeter
