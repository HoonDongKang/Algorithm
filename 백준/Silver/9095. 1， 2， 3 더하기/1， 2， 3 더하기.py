import sys

def sys_input():
  return sys.stdin.readline().rstrip()

def solve(inputs:list[int]) -> list[int]:
  dp = [0] * (max(inputs) + 1)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4

  answers = []

  for input in inputs:
      for i in range(4, input+1):
        if dp[i] != 0:
          continue

        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

      answers.append(dp[input])

  return answers

def main():
  n = int(sys_input())
  inputs = list(map(int, [sys_input() for _ in range(n)]))

  answers = solve(inputs)

  for answer in answers:
    print(answer)

if __name__ == "__main__":
  main()
