import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs:list[int]) -> list[int]:
    pass
def main():
    a,b,c = map(int, sys_input().split())
    print(a+b+c)

if __name__ == "__main__":
    main()
