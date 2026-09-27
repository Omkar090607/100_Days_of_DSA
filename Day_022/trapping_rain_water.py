# LeetCode 42 - Trapping Rain Water
# Difficulty: Hard
# Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
# Runtime: 3ms, Beats 94.69%
# Memory: 21.06MB, Beats 50.62%

class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water