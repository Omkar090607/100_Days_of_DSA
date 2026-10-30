# LeetCode - 32. Longest Valid Parentheses
# Difficulty: Hard
# Topics: String, Dynamic Programming, Stack

# Runtime: 7 ms (Beats 91.74%)
# Memory: 20.52 MB (Beats 34.47%)

class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len