n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def quick_sort(arr, left, right):
    if left < right:
        pos = partition(arr, left, right)
        quick_sort(arr, left, pos - 1)
        quick_sort(arr, pos + 1, right)

def partition(arr, left, right):
    pivot_idx = (left + right) // 2
    pivot_val = arr[pivot_idx]
    
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    
    i = left - 1 
    for j in range(left, right):
        if arr[j] < pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

quick_sort(arr, 0, n-1)
print(*arr)