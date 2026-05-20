import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

total = a + b + c
average = total // 3
result = total - average

print(total)
print(average)
print(result)