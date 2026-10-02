# LeetCode #47 - Permutations II
# Difficulty: Medium
# Topics: Array, Backtracking, Sorting
# Runtime: 3ms (Beats 90.09%)
# Memory: 19.92MB (Beats 24.01%)

class Solution:
    def permuteUnique(self, nums):
        result = []

        # Sort the array so duplicate numbers are next to each other
        nums.sort()

        def backtrack(path, used):
            # If all numbers are used, add the permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # Skip numbers that are already used
                if used[i]:
                    continue

                # Skip duplicate numbers at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose the current number
                path.append(nums[i])
                used[i] = True

                # Explore the next position
                backtrack(path, used)

                # Undo the choice
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result