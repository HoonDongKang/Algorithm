class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        def countNumbers(prefix):
            count = 0
            next_prefix = prefix + 1
            while prefix <= n:
                count += min(n+1, next_prefix) - prefix
                prefix *= 10
                next_prefix *= 10

            return count

        while k > 0:
            steps = countNumbers(cur)

            if steps <= k:
                cur += 1 
                k -= steps

            else:
                cur *= 10
                k -= 1
        
        return cur