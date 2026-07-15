class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_count = 0
        ten_count = 0

        def giveChange(bill):
            nonlocal five_count
            nonlocal ten_count

            if bill == 5:
                five_count += 1
                return True

            elif bill == 10:
                if not five_count:
                    return False
                else:
                    five_count -= 1
                    ten_count += 1
                    return True
            else:
                if five_count >= 1 and ten_count >= 1:
                    five_count -= 1
                    ten_count -= 1
                    return True
                
                elif five_count >= 3:
                    five_count -= 3
                    return True
                
                else:
                    return False


        for bill in bills:
            if bill > 0:
                isCharged = giveChange(bill)
                if not isCharged:
                    return False

        return True