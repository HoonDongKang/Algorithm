class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder = { 0: -1 }
        total = 0

        for i, num in enumerate(nums):
            total += num
            rest = total % k

            if rest not in remainder:
                remainder[rest] = i
            elif i - remainder[rest] > 1:
                return True
            
        return False
        