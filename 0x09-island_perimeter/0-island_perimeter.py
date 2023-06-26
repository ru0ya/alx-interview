#!/usr/bin/python3
"""
Function to solve the island perimeter problem
"""


def island_perimeter(grid):
    """
    Function that calculates the perimeter of a grid

    Args: Grid(list) - List of lists of integer values
                       to compute the perimeter

    Returns: Perimeter(int) of a grid
    """
    hist = set()
    perimeter = 0

    def dfs(i, j):
        """
        Defines a depth first search

        Args: i(int) - length of cell
              j(int) = height of cell

        Returns: cell
        """
        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in hist:
            return 0

        hist.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i - 1, j)
        perim += dfs(i, j - 1)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                hist = set()
                return dfs(i, j)
    return perimeter
