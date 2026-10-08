# LeetCode - Jump Game
# Difficulty: Medium
# Topics: Array, Greedy, Dynamic Programming
# Runtime: 15ms, Beats 79.36%
# Memory: 20.20MB, Beats 62.72%

class Solution:
    def canJump(self, nums):
        # Keep track of the farthest position we can reach
        farthest = 0

        for i in range(len(nums)):
            # If we cannot reach this position, return False
            if i > farthest:
                return False

            # Update the farthest reachable position
            farthest = max(farthest, i + nums[i])

            # If we can reach the last index, return True
            if farthest >= len(nums) - 1:
                return True

        return True