from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        @lru_cache(None)
        def solve(a, b):
            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):
                # Split without swapping
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    return True

                # Split with swapping
                if solve(a[:i], b[n - i:]) and solve(a[i:], b[:n - i]):
                    return True

            return False

        return solve(s1, s2)