# LeetCode 37 - Sudoku Solver
# Difficulty: Hard
# Topics: Array, Backtracking, Matrix
# Runtime: 3501ms, Beats 5.02%
# Memory: 19.80MB, Beats 20.02%

class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)

                    box = (r // 3) * 3 + (c // 3)
                    boxes[box].add(num)

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        continue

                    box = (r // 3) * 3 + (c // 3)

                    for num in "123456789":
                        if num in rows[r] or num in cols[c] or num in boxes[box]:
                            continue

                        board[r][c] = num
                        rows[r].add(num)
                        cols[c].add(num)
                        boxes[box].add(num)

                        if solve():
                            return True

                        board[r][c] = "."
                        rows[r].remove(num)
                        cols[c].remove(num)
                        boxes[box].remove(num)

                    return False

            return True

        solve()