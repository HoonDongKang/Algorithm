class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                stack.append((cur, num))
                cur = ""
                num = 0

            elif char == ']':
                prev, repeat = stack.pop()
                cur = prev + cur * repeat

            else:
                cur += char

        return cur