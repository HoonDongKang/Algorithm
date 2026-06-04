class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        end = len(s)

        while end > 0:
            prefix = s[:end]

            if prefix == prefix[::-1]:
                suffix = s[end:]
                return suffix[::-1] + s

            end -= 1