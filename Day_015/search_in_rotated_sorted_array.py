# LeetCode 33 - Search in Rotated Sorted Array
# Difficulty: Medium
# Topics: Array, Binary Search
# Runtime: 0ms, Beats 100.00%
# Memory: 19.56MB, Beats 11.02%

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, right part is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1