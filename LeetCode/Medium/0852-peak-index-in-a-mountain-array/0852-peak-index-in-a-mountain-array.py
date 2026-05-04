class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        max_num = max(arr)

        while left < right:
            left_num = arr[left]
            right_num = arr[right]
            if left_num == max_num:
                return left
            if right_num == max_num:
                return right
            left -= 1
            right -= 1

        return 0
            