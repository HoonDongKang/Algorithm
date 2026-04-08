import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n:int, m:int, fields: list[list[int]], coords: list[list[int]]):
    dp = [[0] * (n+1) for _ in range(n+1)]
    result = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = (
                fields[i-1][j-1]
                + dp[i-1][j]
                + dp[i][j-1]
                - dp[i-1][j-1]
            )

    for coord in coords:
        x1,y1,x2,y2 = coord
        sum_num= dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        result.append(str(sum_num))

    return result
def main():
    n, m = map(int, sys_input().split())
    fields = [list(map(int, sys_input().split())) for _ in range(n)]
    coords = [list(map(int, sys_input().split())) for _ in range(m)]
    answers = solve(n, m, fields, coords)
    print("\n".join(answers))
if __name__ == "__main__":
    main()
