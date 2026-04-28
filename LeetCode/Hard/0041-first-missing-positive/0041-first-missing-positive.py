class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_num = sorted(nums)
        small_num = 1

        for num in sorted_num:
            if num <= 0:
                continue
            else:
                if num <= small_num:
                    small_num = num + 1
        return small_num