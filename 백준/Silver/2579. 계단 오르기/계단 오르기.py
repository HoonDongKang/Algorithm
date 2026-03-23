import sys

def sys_input():
  return sys.stdin.readline().rstrip()

def solve(n:int, scores:list[int]) -> int:
  if n == 1:
    return scores[0]
  if n == 2:
      return scores[0] + scores[1]
  
  dp= [0] * (n+1)

  dp[1] = scores[0]
  dp[2] = scores[0] + scores[1]
  dp[3] = max(
    scores[0] + scores[2],
    scores[1] + scores[2]
  )
  
  for i in range(4, n+1):
    dp[i]= max(
      dp[i-2] + scores[i-1],
      dp[i-3] + scores[i-2] + scores[i-1]
  )

  return dp[n]


def main():
  n = int(sys_input())
  scores = list(map(int, [sys_input() for _ in range(n)]))

  answer = solve(n, scores)

  print(answer)

if __name__ == "__main__":
  main()
