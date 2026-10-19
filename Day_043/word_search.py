# LeetCode - Word Search
# Difficulty: Medium
# Topics: Array, String, Backtracking, Depth-First Search
# Runtime: 3446ms, Beats 68.10%
# Memory: 19.33MB, Beats 83.08%

class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def search(i, j, index):
            if index == len(word):
                return True

            if (i < 0 or i >= rows or j < 0 or j >= cols
                    or board[i][j] != word[index]):
                return False

            char = board[i][j]
            board[i][j] = "#"

            found = (
                search(i + 1, j, index + 1) or
                search(i - 1, j, index + 1) or
                search(i, j + 1, index + 1) or
                search(i, j - 1, index + 1)
            )

            board[i][j] = char
            return found

        for i in range(rows):
            for j in range(cols):
                if search(i, j, 0):
                    return True

        return False
