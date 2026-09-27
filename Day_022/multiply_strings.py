# LeetCode 43 - Multiply Strings
# Difficulty: Medium
# Topics: Math, String, Simulation
# Runtime: 41ms, Beats 49.81%
# Memory: 19.34MB, Beats 42.98%

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is 0, the product is 0
        if num1 == "0" or num2 == "0":
            return "0"

        # Result can have at most len(num1) + len(num2) digits
        result = [0] * (len(num1) + len(num2))

        # Multiply each digit of num1 with each digit of num2
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                # Positions for the current multiplication
                position1 = i + j
                position2 = i + j + 1

                product = digit1 * digit2 + result[position2]

                # Store the current digit
                result[position2] = product % 10

                # Add carry to the previous position
                result[position1] += product // 10

        # Remove leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        # Convert the result into a string
        return ''.join(map(str, result[start:]))