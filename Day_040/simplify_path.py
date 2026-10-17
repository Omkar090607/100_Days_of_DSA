# LeetCode - Simplify Path
# Difficulty: Medium
# Topics: String, Stack
# Runtime: 1ms, Beats 51.33%
# Memory: 19.24MB, Beats 65.62%

class Solution:
    def simplifyPath(self, path):
        stack = []

        for part in path.split("/"):
            if part == "" or part == ".":
                continue

            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)