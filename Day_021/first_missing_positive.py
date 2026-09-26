# LeetCode 41 - First Missing Positive
# Difficulty: Hard
# Topics: Array, Hash Table, Sorting
# Runtime: 58ms, Beats 27.43%
# Memory: 30.92MB, Beats 47.10%

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Put each positive number in its correct position.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Find the first missing positive number.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1