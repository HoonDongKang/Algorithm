import sys

def sys_input():
  return sys.stdin.readline().rstrip()

def solve(n:int, lists:list[list[int]]) -> int:
  dp = [[0] * 3 for _ in range(n)]
  dp[0][0] = lists[0][0]
  dp[0][1] = lists[0][1]
  dp[0][2] = lists[0][2]

  for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lists[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lists[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + lists[i][2]

  return min(dp[n-1])
  

def main():
  n = int(sys_input())
  lists = [list(map(int, sys_input().split())) for _ in range(n)]


  answer = solve(n, lists)

  print(answer)

if __name__ == "__main__":
  main()
