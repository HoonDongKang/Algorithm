import sys

def sys_input() -> int:
    return int(sys.stdin.readline().rstrip())

def solve(numbers: list[int]) -> tuple[int, int]:
    max_number = max(numbers)
    index = numbers.index(max_number) + 1

    return (max_number, index)

def main() -> None:
    numbers = [sys_input() for _ in range(9)]
    (max_number, index) = solve(numbers)

    print(max_number)
    print(index)
if __name__ == "__main__":
    main()
