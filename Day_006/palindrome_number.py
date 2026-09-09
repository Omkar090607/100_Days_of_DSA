# LeetCode 9 - Palindrome Number
#
# Difficulty: Easy
#
# Topic: Math
#
# Runtime: 9ms (Beats 45.39%)
#
# Memory: 19.34MB (Beats 19.18%)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            # Extract the last digit
            digit = x % 10

            # Add the digit to the reversed half
            reversed_half = reversed_half * 10 + digit

            # Remove the last digit from x
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10