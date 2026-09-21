# LeetCode 34 - Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Topics: Array, Binary Search
# Runtime: 0ms, Beats 100.00%
# Memory: 20.47MB, Beats 91.76%

class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        first = -1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first, last]