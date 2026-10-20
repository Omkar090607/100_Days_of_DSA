# LeetCode - Container With Most Water
# Difficulty: Medium
# Topics: Array, Two Pointers, Greedy
# Runtime: 53ms, Beats 77.00%
# Memory: 29.51MB, Beats 68.84%

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

# Time Complexity: O(n)
# Space Complexity: O(1)