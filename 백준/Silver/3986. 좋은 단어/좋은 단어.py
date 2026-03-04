import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(words: list[str]) -> int:
    stack = []
    result = 0
    
    for word in words:
        stack = []
        for char in word:
            if stack and stack[-1] == char:
                stack.pop()
            else: 
                stack.append(char)
                
        if not stack:
            result +=1

    return result

def main() -> None:
    length = int(sys_input())
    words = [sys_input() for _ in range(length)]
    answer = solve(words)
    print(answer)

if __name__ == "__main__":
    main()
