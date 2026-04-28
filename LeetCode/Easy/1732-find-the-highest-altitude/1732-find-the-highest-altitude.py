class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_num = 0
        cur = 0
        for num in gain:
            cur += num
            max_num = max(cur, max_num)
        
        return max_num
