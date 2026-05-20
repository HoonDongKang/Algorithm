import sys

input = sys.stdin.readline

a, b = map(int, input().split())

print(int(a>=b))
print(int(a>b))
print(int(a<=b))
print(int(a<b))
print(int(a==b))
print(int(a!=b))