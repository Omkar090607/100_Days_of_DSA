# LeetCode 27 - Remove Element
#
# Difficulty: Easy
#
# Topic: Array, Two Pointers
#
# Runtime: 0ms (Beats 100.00%)
#
# Memory: 19.32MB (Beats 19.73%)

class Solution:
    def removeElement(self, nums, val):
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k