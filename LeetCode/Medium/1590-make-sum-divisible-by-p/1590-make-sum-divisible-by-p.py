class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rest = total % p
        if rest == 0:
            return 0
        
        prefix = 0
        seen = { 0: - 1}
        result = len(nums)
        for i, num in enumerate(nums):
            prefix = (num + prefix) % p
            need = (prefix - total + p) % p
            if need in seen:
                result = min(result, i - seen[need])
            seen[prefix] = i

        return result if result < len(nums) else -1


