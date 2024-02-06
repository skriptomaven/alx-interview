#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid):
    '''
    Returns the perimeter of the island
    described in grid.
    '''
    perimeter = 0
    for i in grid + list(map(list, zip(*grid))):
        for j, k in zip([0] + i, i + [0]):
            perimeter += int(j != k)
    return perimeter
