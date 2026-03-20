import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int]):
    return sorted(inputs)

def main():
    length = int(sys_input())
    inputs = [int(sys_input()) for _ in range(length)]
    answers = solve(inputs)
    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
