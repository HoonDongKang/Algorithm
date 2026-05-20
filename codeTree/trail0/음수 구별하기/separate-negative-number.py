import sys

input = sys.stdin.readline

n = int(input().rstrip())

print(n)
if n < 0:
    print('minus')
