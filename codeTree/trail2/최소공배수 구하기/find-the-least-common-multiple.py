n, m = map(int, input().split())

# Please write your code here.
a = n * m
while m!=0:
    n,m=m,n%m

print(a//n)