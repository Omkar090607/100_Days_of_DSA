# LeetCode 35 - Search Insert Position
# Difficulty: Easy
# Topics: Array, Binary Search
# Runtime: 0ms, Beats 100.00%
# Memory: 20.04MB, Beats 12.10%

class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left