shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 집합 자료형 사용
    # O(N) + O(M) + O(1) = O(N + M)
    menus_set = set(menus)
    for order in orders:            # O(N)
        if order not in menus_set:  # O(M)
            return False            # O(1)
    return True

def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess -1

        current_guess = (current_min + current_max) // 2
          
    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)