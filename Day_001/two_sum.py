# LeetCode 1 - Two Sum
#
# Difficulty: Easy
#
# Topic: Array, Hash Table
#
# Runtime: 0ms (Beats 100.00%)
#
# Memory: 12.95MB (Beats 82.85%)

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]