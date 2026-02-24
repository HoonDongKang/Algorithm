import sys

def sys_input():
    return int(sys.stdin.readline().rstrip())

def solve(nums: list[int]) -> list[int]:
    nums.sort()
    total = sum(nums)
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if total - nums[i] - nums[j] == 100:
                return [nums[k] for k in range(n) if k != i and k != j]

    return []

def main() -> None:
    nums = [sys_input() for _ in range(9)]
    print(*solve(nums), sep="\n")

if __name__ == "__main__":
    main()
