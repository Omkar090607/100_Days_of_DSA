# LeetCode - Spiral Matrix II
# Difficulty: Medium
# Topics: Array, Matrix, Simulation
# Runtime: 0ms, Beats 100.00%
# Memory: 19.36MB, Beats 43.20%

class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        num = 1

        while top <= bottom and left <= right:

            # Fill the top row from left to right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1

            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Fill the bottom row from right to left
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1

            # Fill the left column from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix