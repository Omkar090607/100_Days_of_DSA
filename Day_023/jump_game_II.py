# LeetCode 45 - Jump Game II
# Difficulty: Medium
# Topics: Array, Greedy
# Runtime: 7ms, Beats 52.10%
# Memory: 20.00MB, Beats 93.59%

class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            # Keep track of the farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # We have reached the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps