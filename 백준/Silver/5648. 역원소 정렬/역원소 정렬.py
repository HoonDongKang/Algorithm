import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs: list[str]):
    reversed = list(map(lambda x: int(x[::-1]), inputs))
    return sorted(reversed)

def main():
    first_line =  sys_input().split()
    length, inputs = int(first_line[0]), first_line[1:]
    while len(inputs) < length:
        inputs.extend(sys_input().split())
        
    answers = solve(inputs)
    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
