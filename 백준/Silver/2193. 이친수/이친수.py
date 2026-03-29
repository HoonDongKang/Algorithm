import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(length:int):
    dp = [[0] * 2 for _ in range(length + 1)]

    dp[1][0] = 0
    dp[1][1] = 1

    for i in range(2, length + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    return dp[length][0] + dp[length][1]


def main():
    length =int(sys_input())
    answer = solve(length)

    print(answer)

if __name__ == "__main__":
    main()
