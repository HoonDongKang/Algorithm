class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(x):
            str = ""

            for bit in x:
                if bit == "0":
                    str += "1"
                else:
                    str += "0"

            return str

        def reverse(x):
            return "".join(reversed(x))

        def make(x):
            return x + "1" + reverse(invert(x))

        s = "0"

        for _ in range(n - 1):
            s = make(s)

        return s[k - 1]
