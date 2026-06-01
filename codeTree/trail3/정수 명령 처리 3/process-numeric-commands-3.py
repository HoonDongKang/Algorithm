from collections import deque
import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(commands):
    queue = deque()
    result = []

    for command_line in commands:
        cmd = command_line.split()
        operation = cmd[0]

        if operation == 'push_front':
            queue.appendleft(int(cmd[1]))
        elif operation == 'push_back':
            queue.append(int(cmd[1]))
        elif operation == 'pop_front':
            result.append(queue.popleft())
        elif operation == 'pop_back':
            result.append(queue.pop())
        elif operation == 'size':
            result.append(len(queue))
        elif operation == 'empty':
            result.append(0 if queue else 1)
        elif operation == 'front':
            result.append(queue[0])
        elif operation == 'back':
            result.append(queue[-1])
    
    return result

def main():
    n = int(sys_input())
    inputs = [sys_input() for _ in range(n)]
    
    answers = solve(inputs)
    
    for ans in answers:
        print(ans)


if __name__ == '__main__':
    main()
