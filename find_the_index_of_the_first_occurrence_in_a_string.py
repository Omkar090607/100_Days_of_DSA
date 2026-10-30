# LeetCode - 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Topics: Two Pointers, String

# Runtime: 0 ms (Beats 100.00%)
# Memory: 19.41 MB (Beats 8.49%)

class Solution:
    def strStr(self, haystack, needle):
        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1