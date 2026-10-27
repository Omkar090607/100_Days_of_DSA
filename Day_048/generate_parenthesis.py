# LeetCode - Generate Parentheses
# Difficulty: Medium
# Topics: String, Dynamic Programming, Backtracking
# Runtime: 0ms, Beats 100.00%
# Memory: 19.34MB, Beats 73.88%

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: O(n) auxiliary space