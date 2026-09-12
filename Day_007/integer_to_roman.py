# LeetCode 12 - Integer to Roman
#
# Difficulty: Medium
#
# Topic: Hash Table, Math, String, Greedy
#
# Runtime: 4ms (Beats 60.28%)
#
# Memory: 19.24MB (Beats 65.04%)

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = []

        # Process values from largest to smallest
        for value, symbol in zip(values, symbols):
            # Add the symbol while the value can be used
            while num >= value:
                result.append(symbol)
                num -= value

        # Combine all symbols into the final Roman numeral
        return "".join(result)