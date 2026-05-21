import sys
input = sys.stdin.readline
a, n = map(int, input().split())

for i in range(n):
    a += n
    print(a)