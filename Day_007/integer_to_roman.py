# LeetCode 12 - Integer to Roman
#
# Difficulty: Medium
#
# Topic: Hash Table, Math, String, Greedy
#
# Runtime: 4ms (Beats 60.07%)
#
# Memory: 19.24MB (Beats 65.22%)

class Solution:
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result