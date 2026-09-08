# LeetCode 5 - Longest Palindromic Substring
#
# Difficulty: Medium
#
# Topic: String, Dynamic Programming, Two Pointers
#
# Runtime: 252ms (Beats 62.03%)
#
# Memory: 19.44MB (Beats 18.32%)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            # Expand while the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindrome
            l1, r1 = expand(i, i)

            # Even length palindrome
            l2, r2 = expand(i, i + 1)

            # Update longest odd palindrome
            if r1 - l1 + 1 > max_len:
                start = l1
                max_len = r1 - l1 + 1

            # Update longest even palindrome
            if r2 - l2 + 1 > max_len:
                start = l2
                max_len = r2 - l2 + 1

        return s[start:start + max_len]