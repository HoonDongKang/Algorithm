def solution(clothes):
    clothes_obj = {}
    total = 1

    for cloth in clothes:
        _, category = cloth
        if not category in clothes_obj:
            clothes_obj[category] = 0
            
        clothes_obj[category] += 1

    for count in clothes_obj.values():
        total *= (count + 1)

    return total - 1
   
