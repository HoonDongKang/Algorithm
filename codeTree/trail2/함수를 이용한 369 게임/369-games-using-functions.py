a, b = map(int, input().split())

# Please write your code here.

def get_nums(a,b):
    result = []
    for i in range(a,b + 1):
        result.append(i)
    
    return result

def first_rule(n:int):
    str_val = str(n)
    for char in str_val:
        if int(char) in [3,6,9]:
            return True
    
    return False

def get_answer(a,b):
    result = 0
    arr = get_nums(a, b)
    for num in arr:
        if first_rule(num) or num % 3 == 0:
            result += 1

    return result

print(get_answer(a,b)) 