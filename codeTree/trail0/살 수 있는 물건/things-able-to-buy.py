import sys
input = sys.stdin.readline
money = int(input().rstrip())

if money >= 3000:
    print("book")
elif money >= 1000:
    print("mask")
else:
    print("no")