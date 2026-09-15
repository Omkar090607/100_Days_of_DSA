# LeetCode 16 - 3Sum Closest
#
# Difficulty: Medium
#
# Topic: Array, Two Pointers, Sorting
#
# Runtime: 387ms (Beats 47.29%)
#
# Memory: 19.48MB (Beats 15.70%)

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(closest - target):
                    closest = current

                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current

        return closest