# LeetCode 65 - Valid Number
# Difficulty: Hard
# Topics: String
# Runtime: 2ms, Beats 29.72%
# Memory: 19.30MB, Beats 42.06%

class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            # Check for digits
            if ch.isdigit():
                seen_digit = True

            # Check for decimal point
            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            # Check for exponent
            elif ch == 'e' or ch == 'E':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False

            # Check for signs
            elif ch == '+' or ch == '-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            else:
                return False

        return seen_digit