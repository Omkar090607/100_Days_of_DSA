# LeetCode 63 - Unique Paths II
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Matrix
# Runtime: 4ms, Beats 8.18%
# Memory: 19.36MB, Beats 63.17%

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[0] = 1

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]

        return dp[-1]