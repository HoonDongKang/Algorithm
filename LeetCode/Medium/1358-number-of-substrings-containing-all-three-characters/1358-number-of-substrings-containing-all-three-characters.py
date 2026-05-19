class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        n = len(s)
        l = 0
        result = 0
        for r in range(n):
            count[s[r]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                result += (n - r)
                count[s[l]] -= 1
                l += 1
        return result
