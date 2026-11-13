
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        parts = []

        def backtrack(index):
            # If four parts are created, check if all digits are used
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            # Try taking 1, 2, or 3 digits
            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Check for leading zeros
                if len(part) > 1 and part[0] == '0':
                    break

                # Check if the number is valid
                if int(part) > 255:
                    break

                parts.append(part)
                backtrack(index + length)
                parts.pop()

        backtrack(0)
        return result