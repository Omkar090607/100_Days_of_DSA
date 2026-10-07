# LeetCode - Spiral Matrix
# Difficulty: Medium
# Topics: Array, Matrix, Simulation
# Runtime: 0ms, Beats 100.00%
# Memory: 19.36MB, Beats 35.32%

class Solution:
    def spiralOrder(self, matrix):
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Move from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Move from top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Move from right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Move from bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result