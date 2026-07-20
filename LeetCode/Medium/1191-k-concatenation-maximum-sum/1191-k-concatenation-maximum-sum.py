class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        def kadane(arr):
            cur = 0
            best = 0

            for el in arr:
                cur = max(0, cur + el)
                best = max(best, cur)
            
            return best

        if k == 1:
            return kadane(arr)
        
        else:
            answer = kadane(arr+arr)
            if sum(arr) > 0:
                answer += (k-2) * sum(arr)

            return answer % (10**9 + 7)