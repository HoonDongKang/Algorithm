import sys

def sys_input() -> int:
    return int(sys.stdin.readline().rstrip())

def solve(numbers: tuple[int, int]) -> None:
    for a, b in numbers:
        print(a + b)

def main() -> None:
    count = sys_input()
    for n in range(count):
        print('*' * (n+1))
if __name__ == "__main__":
    main()
