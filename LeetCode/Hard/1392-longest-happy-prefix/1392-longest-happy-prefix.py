class Solution:
    def longestPrefix(self, s: str) -> str:
        result = ""

        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[len(s) - i:]

            if prefix == suffix:
                result = prefix

        return result