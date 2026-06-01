from collections import deque
import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n):
    queue = deque()

    for i in range(n):
        queue.append(i+1)

    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())

    return queue[0]
        

def main():
    n = int(sys_input())
    
    answer = solve(n)
    print(answer)

if __name__ == '__main__':
    main()
