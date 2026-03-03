import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int]) -> list[int]:
    queue = deque()
    result = []
    
    for input in inputs:
        splitted_input = input.split()
        command = splitted_input[0]

        if command == 'push':
            queue.append(splitted_input[1])

        elif command == 'front':
            result.append(queue[0] if queue else "-1")

        elif command == 'back':
            result.append(queue[-1] if queue else "-1")
        
        elif command == 'pop':
            result.append(queue.popleft() if queue else "-1")

        elif command == 'size':
            result.append(str(len(queue)))
        
        elif command == 'empty':
            result.append("0" if queue else "1")
        
        else:
            return 0
    return result

def main() -> None:
    length = int(sys_input())
    inputs = [sys_input() for _ in range(length)]
    answer = solve(inputs)
    for i in answer:
        print(i)

if __name__ == "__main__":
    main()
