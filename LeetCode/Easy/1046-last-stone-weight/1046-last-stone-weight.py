import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)        

        while len(stones) > 1 :
            max_stone = -heapq.heappop(stones)
            max_stone_2 = -heapq.heappop(stones)

            if max_stone!=max_stone_2:
                heapq.heappush(stones, -(max_stone - max_stone_2))

        return -stones[0] if stones else 0
