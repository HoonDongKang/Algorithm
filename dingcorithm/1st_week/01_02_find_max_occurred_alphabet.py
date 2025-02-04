def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    # ord = 문자를 아스키코드로 변환
    # chr = 아스키코드를 문자로 변환

    # 1. a,b,c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 알파벳으로 치환한다.
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    #                   "t", "u", "v", "x", "y", "z"]     26개의 공간 사용    
    # max_occurece = 0                                    1개의 공산 사용 
    # max_alphabet = alphabet_array[0]                    1개의 공간 사용

    # for alphabet in alphabet_array:                     array만큼 연산
    #     occurence = 0                                   1개의 공간 사용 / 대입연산

    #     for char in string:                             string만큼 연산
    #         if char == alphabet:                        비교연산
    #             occurence += 1                          대입연산

    #     if occurence > max_occurece:                    비교연산
    #         max_alphabet = alphabet                     대입연산
    #         max_occurece = occurence                    대입연산

    # return max_alphabet

    # 총 29개의 공간 사용
    # 시간복잡도 = 1 + 2 * n + 3

    # 2. 각 알파벳의 빈도수를 저장한 배열을 만들고 해당 알파벳의 인덱스에 해당하는 값을 증가시킨다.
    alphabet_occurrence_array = [0] * 26                  #26개의 공간사용

    for char in string:                                   #string 길이만큼 연산
        if not char.isalpha():                            #비교연산
            continue
      
        arr_index = ord(char) - ord("a")                  #1개의 공간사용 / 대입연산
        alphabet_occurrence_array[arr_index] += 1         #대입연산

    max_occurence = 0                                     #1개의 공간사용 / 대입연산
    max_alphabet_index = 0                                #1개의 공간사용 / 댕ㅂ연산
    
    for index in range(len(alphabet_occurrence_array)):   #alphabet_array만큼 연산
        occurence = alphabet_occurrence_array[index]      #1개의 공간사용 / 대입연산
        if occurence > max_occurence:                     #비교연산
            max_occurence = occurence                     #대입연산
            max_alphabet_index = index                    #대입연산

    return chr(max_alphabet_index + ord("a"))
# 공간복잡도: 30개의 공간 사용
# 시간복잡도 > 공간복잡도 // 공간복잡도 29,30 모두 상수라서 비슷
# 시간복잡도 = n * (1 + 2) + 2 + 26 * (1 + 3) = 3n = 106 -> n
result = find_max_occurred_alphabet
print("Answer = i Current Value =", result("hello my name is dingcodingco"))
print("Answer = e Current Value =", result("we love algorithm"))
print("Answer = b Current Value =", result("best of best youtube"))

# def find_alphabet_occurrence_array(string):
#     alphabet_occurrence_array = [0] * 26

#     for char in string:
#         if not char.isalpha():
#             continue
        
#         arr_index = ord(char) - ord("a")
#         alphabet_occurrence_array[arr_index] += 1

#     return alphabet_occurrence_array


# print("Answer = [3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0] \nCurrent Value =", find_alphabet_occurrence_array("Hello my name is sparta"))
# print("Answer = [2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0] \nCurrent Value =", find_alphabet_occurrence_array("Sparta coding club"))
# print("Answer = [2, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 3, 3, 0, 0, 0, 0, 0, 0] \nCurrent Value =", find_alphabet_occurrence_array("best of best sparta"))