# LeetCode - Text Justification
# Difficulty: Hard
# Topics: Array, String, Greedy, Simulation
# Runtime: 0ms, Beats 100.00%
# Memory: 19.42MB, Beats 17.94%

class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            # Collect as many words as possible for the current line
            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            spaces = maxWidth - length

            # Last line or a line with only one word
            if i == len(words) or len(line) == 1:
                result.append(" ".join(line) + " " * (maxWidth - len(" ".join(line))))
                continue

            gaps = len(line) - 1
            space = spaces // gaps
            extra = spaces % gaps

            current = ""

            for j in range(gaps):
                current += line[j]
                current += " " * (space + (1 if j < extra else 0))

            current += line[-1]
            result.append(current)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)