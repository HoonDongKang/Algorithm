import sys
import math
from collections import Counter

def sys_input() -> int:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int], target:int) -> int:
    inputs.sort()
    answer = 0
    left = 0
    right = len(inputs) - 1

    while left < right:
        total = inputs[left] + inputs[right]
        if total == target:
            answer += 1
            left += 1
            right -= 1

        elif total < target:
            left +=1
        else:
            right -= 1

    return answer


def main() -> None:
    input_count = int(sys_input())
    inputs = list(map(int,sys_input().split()))
    target = int(sys_input())

    answer = solve(inputs, target)
    print(answer)

if __name__ == "__main__":
    main()
