import sys
sys.setrecursionlimit(10**6)

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(num: int):
    dp = [0] * (num + 1)

    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[num]

        

def main():
    num =int(sys_input())
    answer = solve(num)
    print(answer)


if __name__ == "__main__":
    main()
