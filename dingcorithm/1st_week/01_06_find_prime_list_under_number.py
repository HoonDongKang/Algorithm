input = 20
# 소수는 자기 자신과 1외에는 아무 것도 나눌 수 없다.
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!

    # 1. 첫 번째 풀이
    # prime_list = []
    # for n in range(2, number + 1): # 2 ~ n
    #     for i in range(2, n):      # 2 ~ n - 1
    #         if n % i == 0:
    #             break
    #     else:
    #         prime_list.append(n)

    # return prime_list

    # 2. 두 번째 풀이
    # n 보다 작은 모든 소수들로만 나눠보면 된다.

    # 3. 세 번재 풀이
    # N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
    # i * i <= n 일 때까지만 계산
    prime_list = []

    for n in range(2, number + 1):
        for i in range(2, n):
            if i * i <= n and n & i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)