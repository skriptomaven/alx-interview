#!/usr/bin/python3
'''
Change comes from within module.
'''


def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed to meet
    a given amount total given a pile of coins of
    different values.
    '''
    coins = []
    total = len(coins)
    if total <= 0:
        return 0
    if not total:
        return -1
    return fewest_number
