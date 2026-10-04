# LeetCode - Group Anagrams
# Difficulty: Medium
# Topics: Array, Hash Table, String, Sorting
# Runtime: 7ms, Beats 98.34%
# Memory: 21.96MB, Beats 79.36%

class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            # Sort the letters so anagrams get the same key
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())