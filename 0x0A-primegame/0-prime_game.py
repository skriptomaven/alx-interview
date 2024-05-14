#!/usr/bin/python3
'''
Prime Game Module.
'''


def primes(n):
    '''
    Returns a list of prime numbers.
    '''
    prime_numbers = []
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if (sieve[i]):
            prime_numbers.append(i)
            for j in range(i, n + 1, i):
                sieve[j] = False
    return prime_numbers


def isWinner(x, nums):
    '''
    Returns the name of the player that won most rounds.
    '''
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime_number = primes(nums[i])
        if len(prime_number) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
