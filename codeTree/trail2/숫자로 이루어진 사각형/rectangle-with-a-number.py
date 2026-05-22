n = int(input())

# Please write your code here.
def printSquare(n:int):
    for i in range(n):
        row = []
        for j in range(n):
            value = (i*n+j) % 9 + 1
            row.append(str(value))
        print(" ".join(row))

printSquare(n)