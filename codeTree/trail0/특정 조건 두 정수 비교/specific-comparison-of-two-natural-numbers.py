import sys
input = sys.stdin.readline

a,b = map(int, input().split())

c = 1 if a < b else 0
d = 1 if a == b else 0

print(c,d)