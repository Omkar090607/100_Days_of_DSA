# LeetCode - Insert Interval
# Difficulty: Medium
# Topics: Array
# Runtime: 0ms, Beats 100.00%
# Memory: 21.30MB, Beats 58.69%

class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            # Add intervals that come before the new interval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Add the new interval if it comes before the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Merge intervals that overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # Add the remaining interval
        result.append(newInterval)

        return result