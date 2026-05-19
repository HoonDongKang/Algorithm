class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        max_count = 0
        result = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            max_count = max(max_count, count[s[i]])
            while (i - start + 1) - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, i-start + 1)
        
        return result

            

        
            
