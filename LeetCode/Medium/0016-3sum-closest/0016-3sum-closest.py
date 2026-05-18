class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        result = nums[0] + nums[1] + nums[2]
        min_diff = abs(target - result)

        for i in range(len(nums) - 2):
            cur= nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = cur + nums[left] + nums[right]
                diff = abs(target - total)

                if diff < min_diff:
                    min_diff = diff
                    result = total
                
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return total
        return result
