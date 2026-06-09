class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        result = []

        for i, arr in enumerate(intervals):
            starts.append((arr[0], i))

        starts.sort()

        for start, end in intervals:
            left, right = 0, len(starts)

            while left < right:
                mid = (left + right) // 2
                target = starts[mid][0]
                
                if target < end:
                    left = mid + 1

                else:
                    right = mid

            if left == len(starts):
                result.append(-1)
            else:
                result.append(starts[left][1])

        return result