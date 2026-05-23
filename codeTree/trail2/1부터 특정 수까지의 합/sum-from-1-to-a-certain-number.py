n = int(input())

# Please write your code here.

def addFunc(n:int):
    result = 0
    for i in range(1, n+1):
        result += i
    
    return result // 10

print(addFunc(n))