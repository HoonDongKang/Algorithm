import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int]):
    count = {}
    
    for i, num in enumerate(inputs):
        if num not in count:
            count[num] = [0, i]
        count[num][0] += 1

    result = sorted(count, key=lambda x: (-count[x][0], count[x][1]))
    answer = []

    for num in result:
        answer.extend([num] * count[num][0])
        
    return answer

def main():
    length, num = map(int, sys_input().split())
    inputs = list(map(int, sys_input().split()))
    answers = solve(inputs)
    print(*answers)


if __name__ == "__main__":
    main()
