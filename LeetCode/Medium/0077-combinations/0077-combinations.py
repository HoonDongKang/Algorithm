class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        stack = []

        def dfs(start):
            if len(stack) == k:
                result.append(stack[:])
                return
            
            for num in range(start, n+1):
                stack.append(num)
                dfs(num + 1)
                stack.pop()

        dfs(1)
        return result