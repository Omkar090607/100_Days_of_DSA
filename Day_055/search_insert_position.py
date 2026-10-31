# LeetCode - 35. Search Insert Position
# Difficulty: Easy
# Topics: Array, Binary Search

# Runtime: 0 ms (Beats 100.00%)
# Memory: 20.04 MB (Beats 10.13%)

class Solution:
    def searchInsert(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left