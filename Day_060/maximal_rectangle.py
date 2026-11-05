class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Update the heights for this row
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Find the largest rectangle in the histogram
            stack = []

            for i in range(cols + 1):
                current = heights[i] if i < cols else 0

                while stack and heights[stack[-1]] > current:
                    height = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    max_area = max(max_area, height * width)

                stack.append(i)

        return max_area