class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        map_nums = dict()
        sorted_nums = sorted(nums)
        result = []
        
        for i, num in enumerate(sorted_nums):
            if num not in map_nums:
                map_nums[num] = i
        
        for num in nums:
            result.append(map_nums[num])

        return result