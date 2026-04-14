import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, m:int, nums:list[tuple[int,int]]):
    return n-1
    
def main():
    result = []
    t = int(sys_input())

    for _ in range(t):
        n,m = map(int,sys_input().split())
        nums = [tuple(map(int,sys_input().split())) for _ in range(m)]
        result.append(solve(n,m,nums))

    [print(result[i]) for i in range(len(result))]

if __name__ == "__main__":
    main()
