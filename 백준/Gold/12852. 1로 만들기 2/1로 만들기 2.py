import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int):
    dp = [0] * (n+1)
    prev = [0] * (n+1)
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        prev[i] = i -1 
        if i % 2 == 0:
            if dp[i] > dp[i//2] + 1:
                dp[i] = min(dp[i], dp[i//2] + 1)
                prev[i] = i // 2

        if i % 3 == 0:
            if dp[i] > dp[i//3] + 1:
                dp[i] = min(dp[i], dp[i//3] + 1)
                prev[i] = i // 3

    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = prev[cur]

    return dp[n], path
    
def main():
    n = int(sys_input())
    cnt, path = solve(n)

    print(cnt)
    print(*path)

if __name__ == "__main__":
    main()
