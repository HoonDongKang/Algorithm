import sys

MEMO = {}

def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n:int, juices: list[int]):
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = juices[0]
    dp[0][2] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i-1][0] + juices[i]
        dp[i][2] = dp[i-1][1] + juices[i]

    return max(dp[n-1])

def main():
    n = int(sys_input())
    juices = [int(sys_input()) for _ in range(n)]

    answer = solve(n, juices)
    print(answer)
if __name__ == "__main__":
    main()
