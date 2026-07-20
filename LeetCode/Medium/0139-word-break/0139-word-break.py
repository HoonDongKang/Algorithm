class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        def dfs(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    if dfs(end):
                        memo[start] = True
                        return True
                    
            memo[start] = False
            return False
        
        return dfs(0)