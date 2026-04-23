from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        queue = deque(students)
        stack = list(reversed(sandwiches))
        fail = 0

        while stack:
            student = queue.popleft()
            if student == stack[-1]:
                stack.pop()
                fail = 0
            else:
                queue.append(student)
                fail += 1

            if fail == len(queue):
                break
        
        return len(queue)
