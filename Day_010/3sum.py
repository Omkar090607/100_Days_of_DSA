# LeetCode 15 - 3Sum
#
# Difficulty: Medium
#
# Topic: Array, Two Pointers, Sorting
#
# Runtime: 651ms (Beats 42.79%)
#
# Memory: 22.07MB (Beats 94.31%)

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans
    