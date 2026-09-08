# LeetCode 6 - Zigzag Conversion

#Difficulty: Medium**
#Topic: String**
#Runtime: 10ms (Beats 55.44%)**
#Memory: 19.32MB (Beats 46.49%)**

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr_row = 0
        direction = -1

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1

            curr_row += direction

        return ''.join(rows)