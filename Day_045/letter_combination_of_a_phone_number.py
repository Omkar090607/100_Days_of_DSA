# LeetCode - Letter Combinations of a Phone Number
# Difficulty: Medium
# Topics: Hash Table, String, Backtracking
# Runtime: 0ms, Beats 100.00%
# Memory: 19.25MB, Beats 76.76%

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return

            for letter in phone[digits[index]]:
                backtrack(index + 1, current + letter)

        backtrack(0, "")

        return result

# Time Complexity: O(4^n * n)
# Space Complexity: O(n) auxiliary space