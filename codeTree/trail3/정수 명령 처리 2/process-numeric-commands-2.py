from collections import deque
N = int(input())
command = []
A = []


# Please write your code here

class Queue:
    def __init__(self):          # 빈 큐 하나를 생성합니다.
        self.dq = deque()
                
    def push(self, item):        # 큐의 맨 뒤에 데이터를 추가합니다.
        self.dq.append(item)
                
    def empty(self):             # 큐가 비어있으면 True를 반환합니다.
        return not self.dq
                
    def size(self):              # 큐에 들어있는 데이터 수를 반환합니다.
        return len(self.dq)
        
    def pop(self):               # 큐의 맨 앞에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Queue is empty")
            
        return self.dq.popleft()
                
    def front(self):             # 큐의 맨 앞에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Queue is empty")
                        
        return self.dq[0]



queue = Queue()
for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        queue.push(line[1])
    elif line[0] == "pop":
        print(queue.pop())
    elif line[0] == "size":
        print(queue.size())
    elif line[0] == "empty":
        print(1 if queue.empty() else 0)
    elif line[0] == "front":
        print(queue.front())
