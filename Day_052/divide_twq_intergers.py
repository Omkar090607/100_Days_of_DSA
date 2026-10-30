# LeetCode - 29. Divide Two Integers
# Difficulty: Medium
# Topics: Math, Bit Manipulation

# Runtime: 0 ms (Beats 100.00%)
# Memory: 19.31 MB (Beats 22.71%)

class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract the largest possible multiples
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp += temp
                multiple += multiple

            dividend -= temp
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        return quotient