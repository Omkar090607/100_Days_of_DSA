# LeetCode - Maximum Subarray
# Difficulty: Medium
# Topics: Array, Divide and Conquer, Dynamic Programming
# Runtime: 35ms, Beats 62.96%
# Memory: 31.26MB, Beats 95.00%

class Solution:
    def maxSubArray(self, nums):
        # Start with the first element
        current_sum = nums[0]
        max_sum = nums[0]

        # Check the remaining elements
        for i in range(1, len(nums)):
            # Either start a new subarray or continue the current one
            current_sum = max(nums[i], current_sum + nums[i])

            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum