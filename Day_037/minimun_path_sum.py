# LeetCode 64 - Minimum Path Sum
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Matrix
# Runtime: 11ms, Beats 55.25%
# Memory: 21.43MB, Beats 67.45%

class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # Calculate the minimum path sum for each cell
        for i in range(rows):
            for j in range(cols):

                # Skip the starting cell
                if i == 0 and j == 0:
                    continue

                # Add the value from the left cell
                if i == 0:
                    grid[i][j] += grid[i][j - 1]

                # Add the value from the cell above
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]

                # Choose the minimum path from above or left
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]