class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_num = set()
        duplicate_num=0

        for i, seen in enumerate(nums):
            if seen in set_num:
                duplicate_num = seen
            set_num.add(seen)

        for i in range(1, len(nums) + 1):
            if i not in set_num:
                return [duplicate_num, i]

            
