
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]

        for i in range(n):
            size = len(ans)

            for j in range(size - 1, -1, -1):
                ans.append(ans[j] | (1 << i))

        return ans