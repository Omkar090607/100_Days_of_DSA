
# LeetCode - 30. Substring with Concatenation of All Words
# Difficulty: Hard
# Topics: Hash Table, String, Sliding Window

# Runtime: 19 ms (Beats 92.76%)
# Memory: 19.89 MB (Beats 64.94%)

class Solution:
    def findSubstring(self, s, words):
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        target = {}

        for word in words:
            target[word] = target.get(word, 0) + 1

        ans = []

        for start in range(word_len):
            left = start
            right = start
            count = 0
            seen = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in target:
                    seen = {}
                    count = 0
                    left = right
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > target[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == word_count:
                    ans.append(left)

                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

        return ans
