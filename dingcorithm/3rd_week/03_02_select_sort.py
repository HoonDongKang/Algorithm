input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    # O(N^2)
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("Answer = [1, 2, 4, 6, 9] / Current value = ",selection_sort([4, 6, 2, 9, 1]))
print("Answer = [-1, 3, 9, 17] / Current value = ",selection_sort([3,-1,17,9]))
print("Answer = [-3, 32, 44, 56, 100] / Current value = ",selection_sort([100,56,-3,32,44]))