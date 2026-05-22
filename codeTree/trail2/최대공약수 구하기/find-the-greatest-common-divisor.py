n, m = map(int, input().split())

# Please write your code here.
while m != 0:
    n, m = m, n % m

print(n)
    