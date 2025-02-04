# 빅오 -> 최악의 경우
# 빅오메가 -> 최선의 경우

def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for element in array:           # Array만큼 연산
        if number == element:       # 비교연산
            return True             # 시간복잡도는 N만큼 걸린다.
    return False


result = is_number_exist
print("Answer = True Current Value =", result(3, [3,5,6,1,2,4]))
# 최선의 경우에는 시간복잡도가 1이다. Ω(1)

print("Answer = True Current Value =", result(4, [3,5,6,1,2,4]))
# 최악의 경우에는 시간복잡도가 N이다 O(N)

# 최악의 경우를 대비해서 알고리즘의 성능을 파악해야 한다. => 빅오 표기법 사용
print("Answer = Flase Current Value =", result(7, [6,6,6]))
print("Answer = True Current Value =", result(2, [6,9,2,7,1888]))