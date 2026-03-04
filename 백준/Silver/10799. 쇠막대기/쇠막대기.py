import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(braces: list[str]) -> int:
    stack = []
    result = 0
    prev_brace = ''

    for brace in braces:
        if brace == "(":
            stack.append(brace)
        else:
            stack.pop()
            if prev_brace == ')':
                result += 1
            else:
                result += len(stack)
        prev_brace = brace
    return result

def main() -> None:
    braces = sys_input()
    answer = solve(braces)
    print(answer)

if __name__ == "__main__":
    main()
