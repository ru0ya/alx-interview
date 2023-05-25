#!/usr/bin/python3
"""
program that solves the N queens problem.
"""
import sys


def nqueens(N):
    """
    Solve the N Queens problem using backtracking.
    Place N queens on an N by N board so that
    no queens are attacking each other.
    Return all possible solutions as a list of lists.
    """
    solutions = []

    def backtrack(y, board):
        """
        Recursive function to perform backtracking
        """
        if y == N:
            solutions.append(list(board))
            return

        for x in range(N):
            if is_safe(x, y, board):
                board.append([x, y])
                backtrack(y + 1, board)
                board.pop()

    def is_safe(x, y, board):
        """
        checks if placing queen on positon x,y is safe
        """
        for q in board:
            qx, qy = q
            if x == qx or y == qy or abs(x - qx) == abs(y - qy):
                return False
        return True

    backtrack(0, [])

    return solutions


def main():
    """
    validates command line arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens_solutions = nqueens(N)
    for solution in queens_solutions:
        for row, col in solution:
            print(f"[{row}, {col}]")
        print()


if __name__ == '__main__':
    main()
