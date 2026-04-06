import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, target:int, num_list:list[int]):
    count= 0
    result = -1

    def merge(num_list:list[int], left: int, mid:int, right:int):
        i = left
        j = mid + 1
        nonlocal count, result
        sorted_arr = []

        while i <= mid and j<= right:
            if num_list[i] <= num_list[j]:
                sorted_arr.append(num_list[i])
                i +=1
            else :
                sorted_arr.append(num_list[j])
                j +=1

        while i <= mid:
            sorted_arr.append(num_list[i])
            i +=1
        while j <= right:
            sorted_arr.append(num_list[j])
            j +=1

        for idx in range(len(sorted_arr)):
            count += 1
            if count == target:
                result = sorted_arr[idx]
                break
            
            num_list[left + idx] = sorted_arr[idx]
        
    def merge_sort(num_list:list[int], left: int, right:int):
        if left < right:
            mid = (left + right)//2
            merge_sort(num_list, left, mid)
            merge_sort(num_list, mid + 1, right)
            merge(num_list, left, mid, right)

            
    merge_sort(num_list, 0, n-1)
    return result

def main():
    n, target = map(int, sys_input().split())
    num_list = list(map(int, sys_input().split()))

    answer = solve(n, target, num_list)
    print(answer)

if __name__ == "__main__":
    main()
