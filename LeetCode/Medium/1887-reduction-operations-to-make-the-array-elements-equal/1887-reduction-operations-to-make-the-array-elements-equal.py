class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        min_num = sorted_nums[0]
        changed = 0
        cur= min_num
        result = 0

        if min_num == sorted_nums[len(nums) - 1]:
            return 0
        
        for i, num in enumerate(sorted_nums):
            if num == min_num:
                continue

            if cur != num:
                cur = num
                changed += 1
            
            result += changed

        return result
