n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        return merge(arr,left,mid,right)

def merge(arr, left, mid, right):
    i,j = left,mid+1
    sorted_arr = []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j+=1

    while i <= mid:
        sorted_arr.append(arr[i])
        i+=1
    
    while j <= right:
        sorted_arr.append(arr[j])
        j+=1

    for k in range(len(sorted_arr)):
        arr[left + k] = sorted_arr[k]
    
    return sorted_arr

print(*merge_sort(arr, 0 , n-1))