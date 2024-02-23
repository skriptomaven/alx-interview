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
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    tmp, numberOfCoins = (0, 0)
    copyTotalCoins = total
    lenCoins = len(coins)

    while(tmp < lenCoins and copyTotalCoins > 0):
        if (copyTotalCoins - coins[tmp]) >= 0:
            copyTotalCoins -= coins[tmp]
            numberOfCoins += 1
        else:
            tmp += 1

    check = copyTotalCoins > 0 and numberOfCoins > 0
    if check or numberOfCoins == 0:
        return -1
    else:
        return numberOfCoins
