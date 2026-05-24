a, b = map(int, input().split())

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

def is_even(n):
    result = 0

    for char in str(n):
        result += int(char)

    return result % 2 == 0

count = 0

for i in range(a, b + 1):
    if is_prime(i) and is_even(i):
        count += 1

print(count)