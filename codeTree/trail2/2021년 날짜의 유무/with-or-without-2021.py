M, D = map(int, input().split())

# Please write your code here.
def is_true(m,d):
    if m <= 0 or m >= 13:
        return 'No'

    if d <= 0 or d >= 32:
        return 'No'
    
    if m == 2 and d >= 29:
        return 'No'

    if m <= 7:
        if m % 2 == 0 and d >= 31:
            return 'No'
    else:
        if m % 2 != 0 and d >= 31:
            return 'No'

    return 'Yes'

print(is_true(M,D))