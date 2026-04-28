class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_num = set(nums)
        small_num = 1

        while True:
            if small_num not in set_num:
                return small_num
            small_num += 1