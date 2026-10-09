# LeetCode - Merge Intervals
# Difficulty: Medium
# Topics: Array, Sorting
# Runtime: 8ms, Beats 44.09%
# Memory: 22.50MB, Beats 61.55%

class Solution:
    def merge(self, intervals):
        # Sort intervals by their starting point
        intervals.sort()

        merged = []

        for interval in intervals:
            # Add the interval if it doesn't overlap with the last one
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Extend the last interval if they overlap
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged