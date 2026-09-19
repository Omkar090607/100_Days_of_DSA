# LeetCode 31 - Next Permutation
#
# Difficulty: Medium
#
# Topic: Array, Two Pointers
#
# Runtime: 0ms (Beats 100.00%)
#
# Memory: 19.23MB (Beats 67.62%)

class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1