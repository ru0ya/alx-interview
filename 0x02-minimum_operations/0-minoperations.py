#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """
    function that calculates the fewest
    number of operations needed to result in
    n H characters in a file

    Parameters: n(int)

    Returns: count of operations
    """
    if n < 1:
        return 0

    x = 2
    count = []
    while x <= int(n ** 0.5):
        if (n % x == 0):
            count.append(x)
            n //= x
        else:
            x += 1

    if (n > 1):
        count.append(n)

    return sum(count)
