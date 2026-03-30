import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs:list[int], length: int):
    dp = [0] * (length + 1)
    dp[0] = inputs[0]
    for i in range(1, length):
        max_val = 0

        for j in range(0, i):
            if inputs[j] < inputs[i]:
                max_val = max(max_val, dp[j]) 

        dp[i] = inputs[i] + max_val

    return max(dp)

def main():
    length =int(sys_input())
    inputs = list(map(int, sys_input().split()))

    answer = solve(inputs, length)
    print(answer)

if __name__ == "__main__":
    main()
