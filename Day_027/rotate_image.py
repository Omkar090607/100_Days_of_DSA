# LeetCode - Rotate Image
# Difficulty: Medium
# Topics: Array, Math, Matrix
# Runtime: 0ms, Beats 100.00%
# Memory: 19.41MB, Beats 6.28%

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # First transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Then reverse each row
        for i in range(n):
            matrix[i].reverse()