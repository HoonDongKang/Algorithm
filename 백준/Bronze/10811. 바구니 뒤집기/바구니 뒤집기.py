import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, inputs:list[list[int]]) -> list[int]:
    arr = [i + 1 for i in range(n)]

    for start, end in inputs:
        arr[start-1:end] = arr[start-1:end][::-1]

    return arr
def main():
    n, m = map(int, sys_input().split());
    inputs = [list(map(int, sys_input().split())) for _ in range(m)]
    
    answer = solve(n, inputs)
    print(*answer)


if __name__ == "__main__":
    main()
