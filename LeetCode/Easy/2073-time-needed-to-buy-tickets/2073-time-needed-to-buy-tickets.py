from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque((ticket, i) for i,ticket in enumerate(tickets))
        time = 0

        while queue:
            ticket, i = queue.popleft()

            ticket -= 1
            time += 1

            if i == k and ticket == 0:
                return time
            
            if ticket > 0:
                queue.append((ticket, i))

        return time