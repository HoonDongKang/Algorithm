import sys

def sys_input():
    return map(int, sys.stdin.readline().rstrip().split())

def main() -> None:
    a, b = sys_input()
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)

if __name__ == "__main__":
    main()