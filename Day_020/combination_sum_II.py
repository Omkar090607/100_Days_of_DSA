# LeetCode 40 - Combination Sum II
# Difficulty: Medium
# Topics: Array, Backtracking
# Runtime: 3ms, Beats 83.72%
# Memory: 19.35MB, Beats 90.85%

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])

                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result