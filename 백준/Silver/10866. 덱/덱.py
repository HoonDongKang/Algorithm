import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n: int, cmds:list[str]):
    queue = deque()
    result = []

    for command in cmds:
        c = command.split()
        if c[0] == 'push_back':
            queue.append(c[1])
        elif c[0] == 'push_front':
            queue.appendleft(c[1])
        elif c[0] == 'pop_front':
            result.append(queue.popleft() if queue else -1)
        elif c[0] == 'front':
            result.append(queue[0] if queue else -1)
        elif c[0] == 'pop_back':
            result.append(queue.pop() if queue else -1)
        elif c[0] == 'back':
            result.append(queue[-1] if queue else -1) 
        elif c[0] == 'size':
            result.append(len(queue))
        elif c[0] == 'empty':
            result.append(0 if queue else 1)

    return result
def main():
    n = int(sys_input())
    cmds = [sys_input() for _ in range(n)]

    answers = solve(n, cmds)

    for a in answers:
        print(a)

if __name__ == "__main__":
    main()
