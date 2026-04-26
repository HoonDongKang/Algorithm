from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        queue= deque(s)
        for _ in range(len(s)):
            char = queue.popleft()
            queue.append(char)
            if goal == "".join(queue):
                return True
        return False