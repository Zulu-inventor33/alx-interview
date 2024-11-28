#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """Checking if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        # Check column and diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solving the N Queens puzzle andd printing all solutions."""
    board = [-1] * n  # Initialize the board with no queens placed
    solutions = []

    def backtrack(row):
        if row == n:
            # Found a solution, add it to the solutions list
            solutions.append([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    backtrack(0)
    return solutions


def main():
    """Main function that handles input and output."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
