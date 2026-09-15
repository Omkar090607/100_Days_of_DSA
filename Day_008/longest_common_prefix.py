# LeetCode 14 - Longest Common Prefix
#
# Difficulty: Easy
#
# Topic: Array, String
#
# Runtime: 0ms (Beats 100.00%)
#
# Memory: 19.35MB (Beats 31.96%)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Compare the prefix with every remaining word
        for word in strs[1:]:

            # Remove characters until the word starts with the prefix
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                

                # If no common prefix remains, return an empty string
                if not prefix:
                    return ""

        return prefix