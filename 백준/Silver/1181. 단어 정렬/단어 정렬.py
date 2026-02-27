import sys
import math
from collections import Counter

def sys_input() -> int:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[str]) -> list[str]:
    return sorted(set(inputs), key=lambda x: (len(x), x))
def main() -> None:
    input_count = int(sys_input())
    inputs = [sys_input() for _ in range(input_count)]
    sorted_inputs = solve(inputs)

    for input in sorted_inputs:
        print(input)

if __name__ == "__main__":
    main()
