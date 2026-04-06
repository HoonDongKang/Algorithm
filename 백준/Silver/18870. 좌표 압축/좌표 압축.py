import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(number_list:list[str]):
    sorted_set = sorted(set(number_list))
    compress = {value:idx for idx,value in enumerate(sorted_set)}
    result = []

    for n in number_list:
        result.append(compress[n])

    return result

def main():
    n = int(sys_input())
    number_list =  list(map(int, sys_input().split()))

    answers = solve(number_list)
    print(*answers)

if __name__ == "__main__":
    main()
