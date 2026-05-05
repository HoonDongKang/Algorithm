class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
