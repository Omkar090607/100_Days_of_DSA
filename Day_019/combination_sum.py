# LeetCode 39 - Combination Sum
# Difficulty: Medium
# Topics: Array, Backtracking
# Runtime: 7ms, Beats 73.00%
# Memory: 19.60MB, Beats 66.81%

class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                backtrack(i, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)

        return result