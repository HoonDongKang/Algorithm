class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        count = 0
        idx=0
        while idx < len(nums):
            if nums[idx] != 1:
                idx += 1
            else:
                while idx < len(nums) and nums[idx] == 1 :
                    idx += 1
                    count += 1
                    max_count = max(count, max_count)
                count = 0

        return max_count
