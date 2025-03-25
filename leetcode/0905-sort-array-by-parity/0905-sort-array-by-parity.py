class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_pointer = 0
        right_pointer = len(nums) -1

        while left_pointer < right_pointer:
            if nums[left_pointer] % 2 != 0 and nums[right_pointer] % 2 == 0:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]

            if nums[left_pointer] % 2 == 0:
                left_pointer += 1

            if nums[right_pointer] % 2 != 0:
                right_pointer -= 1

        return nums