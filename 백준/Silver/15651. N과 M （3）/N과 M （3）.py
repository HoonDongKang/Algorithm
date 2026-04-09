import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n:int, m: int):
    result = []
    def dfs(idx, cur):
        if idx == m:
            result.append(cur[:])
            return
        for i in range(1, n+1):
            cur.append(i)
            dfs(idx+1, cur)
            cur.pop()
    
    dfs(0, [])
    return result

def main():
    n, m  =  map(int, sys_input().split())
    answers = solve(n, m)
    for row in answers:
        print(*row)

if __name__ == "__main__":
    main()
