#!/usr/bin/python3
"""
A function module
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    list_of_lists = []
    if n <= 0:
        return list_of_lists
    list_of_lists = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(list_of_lists[i - 1]) - 1):
            tmp.append(list_of_lists[i - 1][j] + list_of_lists[i - 1][j + 1])
        tmp.append(1)
        list_of_lists.append(tmp)
    return list_of_lists
