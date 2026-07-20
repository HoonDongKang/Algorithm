class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(i, j):
            k = i + j
            if k == len(s3):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]

            answer = False

            if i < len(s1) and s1[i] == s3[k]:
                answer = answer or dfs(i + 1, j)

            if j < len(s2) and s2[j] == s3[k]:
                answer = answer or dfs(i, j + 1)

            memo[(i,j)] = answer

            return answer

        
        return dfs(0,0)