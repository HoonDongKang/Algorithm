class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        def dfs(index, cur_sum):
            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]
            if index == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            
            plus = dfs(index + 1, cur_sum + nums[index])
            minus = dfs(index + 1, cur_sum - nums[index])

            memo[(index, cur_sum)] = plus + minus
            return memo[(index, cur_sum)]

        return dfs(0,0)