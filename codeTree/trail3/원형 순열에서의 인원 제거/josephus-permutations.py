from collections import deque
import sys

def sys_input():
    return sys.stdin.readline().split()

# Please write your code here.
def solve(n:int ,k:int):
    queue = deque()
    result = []
    
    for i in range(n):
        queue.append(i+1)

    while len(queue):
        for i in range(k):
            next = queue.popleft()
            queue.append(next)
        delete_node = queue.pop()
        result.append(delete_node)

    return result
    
def main():
    n, k = map(int, sys_input())
    print(*solve(n,k))

if __name__ == '__main__':
    main()


