n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    min = i
    for j in range(i, n):
        if arr[j] < arr[min]:
            min = j
    tmp = arr[i]
    arr[i] = arr[min]
    arr[min] = tmp

print(*arr)
            
