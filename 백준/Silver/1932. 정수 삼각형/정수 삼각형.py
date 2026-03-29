import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(cases: list[list[int]], length:int):
    dp = [[0] * (i + 1) for i in range(length)]

    dp[0][0] = cases[0][0]

    for i in range(1, length):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + cases[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + cases[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + cases[i][j]
    
    return max(dp[length -1])


def main():
    length =int(sys_input())
    cases = [list(map(int, sys_input().split())) for _ in range(length)]
    answer = solve(cases, length)

    print(answer)

if __name__ == "__main__":
    main()
