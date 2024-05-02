#!/usr/bin/python3
"""
Making a change module.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total:

        - if total is 0 or less, return 0
        - if total cannot be met by any number of coins you have, return -1

    coins: list of the values of the coins in the progression
         : value of the coin will always be an integer greater than 0
    """
    if total <= 0:
        return 0
    checking_coins = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while checking_coins < total:
            checking_coins += i
            tmp += 1
        if checking_coins == total:
            return tmp
        checking_coins -= i
        tmp -= 1
    return -1
