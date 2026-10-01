# LeetCode #56 - Merge Intervals
# Difficulty: Medium
# Topics: Array, Sorting
# Runtime: 8ms (Beats 43.88%)
# Memory: 22.50MB (Beats 61.15%)

class Solution:
    def merge(self, intervals):
        intervals.sort()

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged