input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # O(N^2)
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

insertion_sort(input)
print(input)

print("Answer = [4, 5, 7, 7, 8] / Current Value = ",insertion_sort([5,8,4,7,7]))
print("Answer = [-1, 3, 9, 17] / Current Value = ",insertion_sort([3,-1,17,9]))
print("Answer = [-3, 32, 44, 56, 100] / Current Value = ",insertion_sort([100,56,-3,32,44]))