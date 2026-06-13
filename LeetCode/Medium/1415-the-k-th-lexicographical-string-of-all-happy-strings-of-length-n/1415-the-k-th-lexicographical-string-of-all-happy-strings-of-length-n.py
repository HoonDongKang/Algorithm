class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        char_list = ['a', 'b', 'c']
        result = []

        def dfs(stack):
            if len(stack) == n:
                result.append("".join(stack))
                return

            for char in char_list:
                if not stack or stack[-1] != char:
                    stack.append(char)
                    dfs(stack)
                    stack.pop()
        dfs([])

        if k > len(result):
            return ""
        return result[k-1]