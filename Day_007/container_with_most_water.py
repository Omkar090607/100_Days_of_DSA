# LeetCode 11 - Container With Most Water
#
# Difficulty: Medium
#
# Topic: Array, Two Pointers, Greedy
#
# Runtime: 53ms (Beats 77.94%)
#
# Memory: 29.51MB (Beats 67.61%)

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            # Calculate the area between the two pointers
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area
            maxArea = max(maxArea, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea