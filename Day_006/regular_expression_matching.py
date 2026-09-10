# LeetCode 10 - Regular Expression Matching
#
# Difficulty: Hard
#
# Topic: String, Dynamic Programming, Recursion, Memoization
#
# Runtime: 4ms (Beats 73.40%)
#
# Memory: 20.50MB (Beats 26.04%)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            # Return the previously calculated result
            if (i, j) in memo:
                return memo[(i, j)]

            # If the pattern is completely processed,
            # the string must also be completely processed
            if j == len(p):
                return i == len(s)

            # Check whether the current characters match
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # Check if the next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: '*' matches zero characters
                # Option 2: '*' matches the current character
                answer = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )
            else:
                # Move to the next character in both
                # the string and pattern
                answer = first_match and dp(i + 1, j + 1)

            # Store the result for future use
            memo[(i, j)] = answer

            return answer

        # Start matching from the beginning
        return dp(0, 0)