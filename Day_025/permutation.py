# LeetCode #46 - Permutations
# Difficulty: Medium
# Topics: Array, Backtracking
# Runtime: 0ms (Beats 100.00%)
# Memory: 19.54MB (Beats 36.39%)

class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, used):
            # If the permutation contains all numbers,
            # add a copy to the result
            if len(path) == len(nums):
                result.append(path[:])
                return

            # Try every number that has not been used
            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose the current number
                path.append(nums[i])
                used[i] = True

                # Explore the next position
                backtrack(path, used)

                # Undo the choice for the next possibility
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result