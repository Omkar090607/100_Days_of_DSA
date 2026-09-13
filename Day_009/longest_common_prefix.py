# LeetCode 14 - Longest Common Prefix
#
# Difficulty: Easy
#
# Topic: Array, String
#
# Runtime: 0ms (Beats 100.00%)
#
# Memory: 19.35MB (Beats 32.04%)

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Compare the prefix with each remaining word
        for word in strs[1:]:

            # Remove characters until the word starts with the prefix
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                # If no common prefix remains, return an empty string
                if not prefix:
                    return ""

        return prefix


# Test the solution in VS Code
if __name__ == "__main__":
    solution = Solution()

    strs = ["flower", "flow", "flight"]

    print("Input:", strs)
    print("Output:", solution.longestCommonPrefix(strs))