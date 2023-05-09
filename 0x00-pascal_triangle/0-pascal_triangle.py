#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's Triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    pascal's triangle

    Arguments: n:integer

    Returns: List of lists of integers
    """
    if n <= 0:
        return []

    # starts with the first row
    tri = [[1]]

    # generates the subsequent rows
    for i in range(n - 1):
        temp = [0] + tri[-1] + [0]  # each row starts and ends with 0
        row = []

        # sums each pair of adjacent numbers to get num in new row
        for j in range(len(tri[-1]) + 1):
            row.append(temp[j] + temp[j + 1])  # add adjacent numbers
            tri.append(row)
    return tri
