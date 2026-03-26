import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(num: int):
    if num == 1:
        return 1
    if num == 2:
        return 2
    
    dp = [0] * (num + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, num + 1):
        dp[i] = (dp[i - 1] + dp[i -2]) % 10007

    return dp[num]


def main():
    num =int(sys_input())
    answer = solve(num)
    print(answer)


if __name__ == "__main__":
    main()
