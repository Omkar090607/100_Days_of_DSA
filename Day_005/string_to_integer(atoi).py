# LeetCode 8 - String to Integer (atoi)
#
# Difficulty: Medium
#
# Topic: String, Math
#
# Runtime: 0ms (Beats 100.00%)
#
# Memory: 19.34MB (Beats 43.63%)

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        index = 0
        n = len(s)

        # Skip leading spaces
        while index < n and s[index] == ' ':
            index += 1

        # Check sign
        sign = 1
        if index < n and (s[index] == '+' or s[index] == '-'):
            if s[index] == '-':
                sign = -1
            index += 1

        result = 0

        # Read digits
        while index < n and s[index].isdigit():
            digit = ord(s[index]) - ord('0')

            # Overflow check
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        return sign * result