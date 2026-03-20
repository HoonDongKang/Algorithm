import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(length: int):
    count = [0] * 10001
    for _ in range(length):
        number = int(sys_input())
        count[number] += 1

    return count

def main():
    length = int(sys_input())
    answer = solve(length)

    for i in range(10001):
        for _ in range(answer[i]):
            print(i)

if __name__ == "__main__":
    main()
