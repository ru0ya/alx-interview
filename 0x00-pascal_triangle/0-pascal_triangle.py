#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    returns a list of lists of integers representing
    pascal's triangle

    Arguments: n:integer

    Returns: List of lists of integers
    """
    if n <= 0:
        return 0
    else:
        tri = [[1]]

        for i in range(n - 1):
            temp = [0] + tri[-1] + [0]
            row = []
            for j in range(len(tri[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            tri.append(row)
    return tri
