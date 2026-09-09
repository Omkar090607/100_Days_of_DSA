# LeetCode 7 - Reverse Integer
#
# Difficulty: Medium
#
# Topic: Math
#
# Runtime: 51ms (Beats 24.08%)
#
# Memory: 19.30MB (Beats 31.88%)

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            rev = rev * 10 + digit

        rev *= sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev