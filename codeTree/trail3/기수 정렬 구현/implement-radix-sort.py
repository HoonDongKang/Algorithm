n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = max(arr)

exp = 1
while max_val // exp > 0:
    map_arr = [[] for _ in range(10)]
    for num in arr:
        digit = (num//exp)%10
        map_arr[digit].append(num)

    arr = []
    for sorted_arr in map_arr:
        arr.extend(sorted_arr)

    exp *= 10

print(*arr)