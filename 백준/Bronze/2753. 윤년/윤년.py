import sys

def sys_input() -> int:
    return int(sys.stdin.readline().rstrip())

def solve(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def main() -> None:
    year = sys_input()
    answer = solve(year)
    print(1 if answer else 0 )

if __name__ == "__main__":
    main()