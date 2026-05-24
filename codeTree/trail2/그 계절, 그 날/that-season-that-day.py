Y, M, D = map(int, input().split())

# Please write your code here.

def is_yoon(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True    
            return False
        return True
    return False

def is_valid(y,m,d):
    if m < 1 or m > 13:
        return False
    
    if d < 1 or d > 31:
        return False

    if m <= 7:
        if m % 2 == 0 and d > 30:
            return False
    else:
        if m % 2 != 0 and d > 30: 
            return False

    if m == 2:
        if is_yoon(y):
            if d > 29:
                return False
        else:
            if d > 28:
                return False

    return True
        

def get_season(y,m,d):
    if not is_valid(y,m,d):
        return -1

    if 3 <= m and m <= 5:
        return 'Spring'
    if 6 <= m and m <= 8:
        return 'Summer'
    if 9 <= m and m <= 11:
        return 'Fall'
    if m in [1, 2, 12]:
        return 'Winter'

    return -1

print(get_season(Y,M,D))
