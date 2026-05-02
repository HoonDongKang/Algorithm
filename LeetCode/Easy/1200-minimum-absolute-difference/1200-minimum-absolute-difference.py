class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        sorted_arr = sorted(arr)
        min_diff = float('inf')
        map = {}

        for i,num in enumerate(sorted_arr):
            if i == len(arr) - 1:
                return map[min_diff]
            
            next = sorted_arr[i+1]
            diff = next-num
            min_diff = min(min_diff, diff)

            if diff not in map:
                map[diff] = []
            
            map[diff].append([num,next])

        return map[min_diff]


print(Solution().minimumAbsDifference([40,11,26,27,-20]))
