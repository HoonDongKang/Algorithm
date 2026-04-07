import sys

MEMO = {}

def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n:int, k:int, stuffs: list[tuple[int]]):
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        w,v = stuffs[i-1]
        for weight in range(k + 1):
            if w > weight:
                dp[i][weight] = dp[i-1][weight]
            else:
                dp[i][weight] = max(dp[i-1][weight], dp[i-1][weight-w] + v)

    return dp[n][k]

def main():
    n, k = map(int, sys_input().split())
    stuffs = [tuple(map(int, sys_input().split())) for _ in range(n)]

    answer = solve(n, k, stuffs)
    print(answer)
if __name__ == "__main__":
    main()
