def find_max_num(array):
    # 이 부분을 채워보세요!

    # 하나의 원소를 다른 원소들과 비교해서 최대값인지 분석하는 방법
    # for number in array:                  array 길이 만큼 실행
    #     is_max_num = True               
    #     for compare_number in array:      array 길이 만큼 실행
    #         if number < compare_number:   비교연산1  
    #             is_max_num = False        대입연산
    #     if is_max_num:                    비교연산2
    #         return number
    # 
    # 시간복잡도 : array 길이 * array 길이 * (비교연산1 + 대입연산) = n * n * 2 = 2 * n^2
    # 시간복잡도(참) : array 길이 * 비교연산 1번 = n

    # 총 시간 복잡도 : 2 * n^2 + n

    #  하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법.
    max_num = array[0]                     #대입연산

    for number in array:                   #array 길이만큼
        if number > max_num:               #비교연산
            max_num = number               #대입연산
    return max_num
    
    # max_num 대입연산 1번 => 1
    # array 길이 * (비교연산 + 대입연산) => 2n
    # 총 시간 복잡도 = 2n + 1
    # return max(array)
print("Answer = 6 / Current_Value = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("Answer = 6 / Current_Value = ", find_max_num([6, 6, 6]))
print("Answer = 1888 / Current_Value = ", find_max_num([6, 9, 2, 7, 1888]))

# 시간 복잡도에서 상수는 신경쓰지말고 어느 정도로 증가하는지만 파악
# 2 * n^2 + n => n^2 만큼의 연산
# 2n + 1 => n 만큼의 연산