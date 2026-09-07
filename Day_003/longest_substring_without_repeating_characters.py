# LeetCode 3 - Longest Substring Without Repeating Characters

# Difficulty: Medium

# Topic: String, Sliding Window, Hash Table

# Runtime: 194ms (Beats 52.74%)

# Memory: 19.60MB (Beats 66.49%)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len