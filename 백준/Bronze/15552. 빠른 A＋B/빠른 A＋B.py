import sys

def sys_input() -> int:
    return sys.stdin.readline()

def solve(numbers: tuple[int, int]) -> None:
    for a, b in numbers:
        print(a + b)

def main() -> None:
    count = int(sys_input())
    numbers = [
        tuple(map(int, sys_input().split()))
        for _ in range(count)
    ]
    solve(numbers)

if __name__ == "__main__":
    main()
