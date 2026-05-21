import sys
input = sys.stdin.readline
temperature = int(input().rstrip())

if temperature < 0:
    print("ice")
elif temperature >= 100:
    print("vapor")
else:
    print("water")