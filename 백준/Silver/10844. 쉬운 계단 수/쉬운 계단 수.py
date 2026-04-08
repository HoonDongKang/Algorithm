import sys

MEMO = {}

def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n:int):
    dp = [[0] * 10 for _ in range(n+1)]
    
    for i in range(1, 10):
        dp[1][i] = 1


    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][1]  
        dp[i][9] = dp[i-1][8]  
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    return sum(dp[n]) % 1000000000


def main():
    n = int(sys_input())
    answer = solve(n)
    print(answer)
if __name__ == "__main__":
    main()
