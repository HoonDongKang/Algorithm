def find_max_num(array):
    # 이 부분을 채워보세요!

    # 하나의 원소를 다른 원소들과 비교해서 최대값인지 분석하는 방법
    # for number in array:
    #     is_max_num = True
    #     for compare_number in array:
    #         if number < compare_number:
    #             is_max_num = False
    #     if is_max_num:
    #         return number

    #  하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법.
    max_num = array[0]

    for number in array:
        if number > max_num:
            max_num = number
    return max_num
    
    # return max(array)


print("Answer = 6 / Current_Value = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("Answer = 6 / Current_Value = ", find_max_num([6, 6, 6]))
print("Answer = 1888 / Current_Value = ", find_max_num([6, 9, 2, 7, 1888]))