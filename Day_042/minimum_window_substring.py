# LeetCode - Minimum Window Substring
# Difficulty: Hard
# Topics: Hash Table, String, Sliding Window
# Runtime: 64ms, Beats 65.54%
# Memory: 19.20MB, Beats 99.92%

class Solution:
    def minWindow(self, s, t):
        from collections import Counter

        need = Counter(t)
        left = 0
        missing = len(t)
        start = 0
        min_length = float("inf")

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1

            need[char] -= 1

            while missing == 0:
                if right - left + 1 < min_length:
                    start = left
                    min_length = right - left + 1

                left_char = s[left]
                need[left_char] += 1

                if need[left_char] > 0:
                    missing += 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]

# Time Complexity: O(m + n)
# Space Complexity: O(n)