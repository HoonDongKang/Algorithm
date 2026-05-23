n = int(input())

# Please write your code here.

def is_answer(n:int):
    str_val = str(n)
    count = 0
    for char in str_val:
        count += int(char)
    if n % 2 == 0:
        if count % 5 == 0:
            return 'Yes'
    
    return 'No'

print(is_answer(n))