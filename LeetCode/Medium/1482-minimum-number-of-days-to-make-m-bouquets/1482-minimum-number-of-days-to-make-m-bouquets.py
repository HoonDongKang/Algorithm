class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        
        def can_make(day:int):
            adj_count = 0
            bouquet_count = 0

            for bloom in bloomDay:
                if bloom <= day:
                    adj_count += 1

                    if adj_count == k:
                        bouquet_count += 1
                        adj_count = 0

                else:
                    adj_count = 0

            if bouquet_count >= m:
                return True

            return False
        
        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            if can_make(mid):
                right = mid
            else:
                left = mid + 1

        return left