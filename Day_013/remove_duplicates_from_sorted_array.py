# LeetCode 26 - Remove Duplicates from Sorted Array
#
# Difficulty: Easy
#
# Topic: Array, Two Pointers
#
# Runtime: 2ms (Beats 49.80%)
#
# Memory: 20.69MB (Beats 17.63%)

class Solution:
    def removeDuplicates(self, nums):
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k