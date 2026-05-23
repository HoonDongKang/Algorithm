y = int(input())

# Please write your code here.
def is_moon(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return 'false'
        return 'true'
    return 'false'

print(is_moon(y))