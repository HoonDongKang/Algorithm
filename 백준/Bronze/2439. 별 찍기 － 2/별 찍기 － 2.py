import sys

def sys_input() -> int:
    return int(sys.stdin.readline().rstrip())

def main() -> None:
    count = sys_input()
    for n in range(count):
        length = n + 1
        print(' ' * (count - length) + '*' * length) 
if __name__ == "__main__":
    main()
