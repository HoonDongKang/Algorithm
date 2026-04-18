class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        num_set= set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)

        for i in range(len(nums)):
            if i + 1 not in num_set:
                result.append(i+1)

        return result