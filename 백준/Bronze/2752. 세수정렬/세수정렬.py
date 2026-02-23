import sys
from typing import List

def sys_input() -> List[int]:
    return list(map(int, sys.stdin.readline().rstrip().split()))

def solve(inputs: List[int]) -> List[int]:
    return sorted(inputs)

def main() -> None:
    inputs = sys_input()
    answer = solve(inputs)
    print(*answer)

if __name__ == '__main__':
    main()