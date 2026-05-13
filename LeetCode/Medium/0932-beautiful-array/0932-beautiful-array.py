class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        result = [1]

        while len(result) < n:
            next_result = []

            for x in result:
                if 2 * x - 1 <= n:
                    next_result.append(2 * x - 1)

            for x in result:
                if 2 * x <= n:
                    next_result.append(2 * x)

            result = next_result

        return result
