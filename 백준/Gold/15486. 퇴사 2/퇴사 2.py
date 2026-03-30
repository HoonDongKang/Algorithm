import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs:list[int], length: int):
    dp = [0] * (length + 1)
    for i in range(length):
        t, p = inputs[i]
        dp[i+1] = max(dp[i+1], dp[i])
        if i + t <= length:
            dp[i+t] = max(dp[i+t], dp[i] + p)

    return dp[length]

def main():
    length =int(sys_input())
    inputs = [list(map(int, sys_input().split())) for _ in range(length)]

    answer = solve(inputs, length)
    print(answer)

if __name__ == "__main__":
    main()
