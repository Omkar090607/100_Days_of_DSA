# LeetCode 36 - Valid Sudoku
# Difficulty: Medium
# Topics: Array, Hash Table, Matrix
# Runtime: 3ms, Beats 74.81%
# Memory: 19.16MB, Beats 95.19%

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                num = board[i][j]
                box = (i // 3) * 3 + (j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[box]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        return True