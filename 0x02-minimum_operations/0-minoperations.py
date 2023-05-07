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
    count = 1
    while n > 0:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = n - 1

        count += 1

    return count
