# LeetCode - N-Queens
# Difficulty: Hard
# Topics: Array, Backtracking
# Runtime: 7ms, Beats 96.14%
# Memory: 19.82MB, Beats 11.11%

class Solution:
    def solveNQueens(self, n: int):
        result = []
        board = [["."] * n for _ in range(n)]

        # Keep track of used columns and diagonals
        columns = set()
        diagonal1 = set()  # row - col
        diagonal2 = set()  # row + col

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Skip positions where a queen can be attacked
                if col in columns or row - col in diagonal1 or row + col in diagonal2:
                    continue

                # Place the queen
                board[row][col] = "Q"
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                backtrack(row + 1)

                # Remove the queen and try another position
                board[row][col] = "."
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        backtrack(0)
        return result