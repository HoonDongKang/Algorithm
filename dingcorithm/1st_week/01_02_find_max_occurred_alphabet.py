def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    # ord = 문자를 아스키코드로 변환
    # chr = 아스키코드를 문자로 변환

    # 1. a,b,c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 알파벳으로 치환한다.
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    #                   "t", "u", "v", "x", "y", "z"]
    
    # max_occurece = 0
    # max_alphabet = alphabet_array[0]

    # for alphabet in alphabet_array:
    #     occurence = 0

    #     for char in string:
    #         if char == alphabet:
    #             occurence += 1

    #     if occurence > max_occurece:
    #         max_alphabet = alphabet
    #         max_occurece = occurence

    # return max_alphabet

    # 2. 각 알파벳의 빈도수를 저장한 배열을 만들고 해당 알파벳의 인덱스에 해당하는 값을 증가시킨다.
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
      
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurence = 0
    max_alphabet_index = 0
    
    for index in range(len(alphabet_occurrence_array)):
        occurence = alphabet_occurrence_array[index]
        if occurence > max_occurence:
            max_occurence = occurence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord("a"))

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