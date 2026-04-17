class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx1, idx2 = 0, 0
        result = []
        median = 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
            else:
                result.append(nums2[idx2])
                idx2 += 1

        if idx1 < len(nums1):
            result.extend(nums1[idx1:])
        if idx2 < len(nums2):
            result.extend(nums2[idx2:])

        n = len(result)
        if n % 2 == 1:
            return result[n // 2]
        else:
            return (result[n // 2 - 1] + result[n // 2]) / 2
