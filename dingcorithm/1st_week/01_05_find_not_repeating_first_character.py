input = "abadabac"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

def find_not_repeating_first_character(string):
    # 직접 풀이 (시간복잡도 O(N^2))
    # answer = []
    # inserted = []

    # for char in string:
    #     if char in answer:
    #         answer.remove(char)
    #     else:
    #         if char not in inserted:
    #             answer.append(char)
    #             inserted.append(char)

    # return answer[0] if answer else "_" 

    #  string에서 알파벳 빈도수를 찾는다
    occurrence_array = find_alphabet_occurrence_array(string)       #O(N)
    not_repeating_character_array = []

    for index in range(len(occurrence_array)):
          alphabet_occurrence = occurrence_array[index]
          if alphabet_occurrence == 1:
              not_repeating_character_array.append(chr(index + ord("a")))
    # 빈도수가 1인 알파벳 중에 먼저 나온 값을 찾는다.
    for char in string:                                             #O(N)
        if char in not_repeating_character_array:
            return char
    return "_"

# 시간복잡도 : O(N)
result = find_not_repeating_first_character
print("Answer = d Current Value =", result("abadabac"))
print("Answer = c Current Value =", result("aabbcddd"))
print("Answer =_ Current Value =", result("aaaaaaaa"))
