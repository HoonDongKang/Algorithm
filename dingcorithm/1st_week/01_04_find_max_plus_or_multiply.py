def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    # answer = 0
    # for el in array:
    #     if el <= 1:
    #         answer += el
    #     else:
    #         answer *= el
    # return answer

    plus_or_multiply_sum = 0
    for number in array:
        if number <= 1 or plus_or_multiply_sum <= 1:
            plus_or_multiply_sum += number
        else:
            plus_or_multiply_sum *= number

    return plus_or_multiply_sum

# 시간복잡도 = O(N)

result = find_max_plus_or_multiply
print("Answer = 728 Current Value =", result([0,3,5,6,1,2,4]))
print("Answer = 8820 Current Value =", result([3,2,1,5,9,7,4]))
print("Answer = 270 Current Value =", result([1,1,1,3,3,2,5]))