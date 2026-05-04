class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        while left < right:
            mid = (left + right ) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] < target:
                left += 1
            else:
                right -=1

        return -1
