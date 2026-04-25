import heapq
class Solution:
    def isPossible(self, target: list[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            max_num = -heapq.heappop(heap)
            rest = total - max_num

            if max_num == 1 or rest == 1:
                return True

            if rest == 0 or max_num <= rest:
                return False
            
            prev = max_num % rest
            if prev == 0:
                return False 

            total = rest + prev
            heapq.heappush(heap, -prev)