class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_total = 0
        odd_total = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_total += num
            else:
                odd_total += num

        left_even = 0
        left_odd = 0
        result = 0

        for i,num in enumerate(nums):
            if i % 2 == 0:
                even_total -= num
            else:
                odd_total -= num

            if left_even +  odd_total == left_odd + even_total:
                result += 1

            if i % 2 ==0:
                left_even += num
            else:
                left_odd += num
        return result
