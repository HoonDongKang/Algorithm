import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(length: int, number_list:list[str]):
    if length == 1:
        return number_list[0] * number_list[0]
    
    sorted_number = sorted(number_list)

    return sorted_number[0] * sorted_number[len(sorted_number) - 1]

def main():
    n = int(sys_input())
    number_list =  list(map(int, sys_input().split()))

    answer = solve(n, number_list)
    print(answer)

if __name__ == "__main__":
    main()
