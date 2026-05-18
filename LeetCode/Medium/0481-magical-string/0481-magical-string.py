class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]

        read = 2
        next_num = 1
        ones = 1

        while len(s) < n:
            count = s[read]

            for _ in range(count):
                s.append(next_num)

                if next_num == 1 and len(s) <= n:
                    ones += 1

            next_num = 2 if next_num == 1 else 1
            read += 1

        return ones