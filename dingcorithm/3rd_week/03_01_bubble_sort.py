input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # O(n^2)
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("answer = [1, 2, 4, 6, 9] / current value = ",bubble_sort([4, 6, 2, 9, 1]))
print("answer = [-1, 3, 9, 17] / current value = ",bubble_sort([3,-1,17,9]))
print("answer = [-3, 32, 44, 56, 100] / current value = ",bubble_sort([100,56,-3,32,44]))