a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


result = 0
for i in range(a,b+1):
    if is_prime(i):
        result += i
    
print(result)