class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        max_idx = arr.index(max(arr))
        if max_idx == 0 or max_idx == len(arr) -1:
            return False
        
        for i in range(1, max_idx):
            cur = arr[i]
            prev= arr[i-1]
            if cur <= prev:
                return False

        for i in range(max_idx+1, len(arr)):
            cur = arr[i]
            prev= arr[i-1]
            if prev <= cur:
                return False
            
        return True
