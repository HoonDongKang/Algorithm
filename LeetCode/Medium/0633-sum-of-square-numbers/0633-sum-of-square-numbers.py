import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(math.sqrt(c))
        left = 0

        while left <= right:
            total = left ** 2 + right ** 2
            if total == c:
                return True
            if total < c:
                left += 1
            else:
                right -= 1

        return False