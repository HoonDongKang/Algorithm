
class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        def buildTrie(root, num, max_bit):
            cur = root

            bits = bin(num)[2:].zfill(max_bit)

            for ch in bits:
                bit = int(ch)
                if cur[bit] == -1:
                    cur[bit] = [-1, -1]
                
                cur = cur[bit]

            return root
        
        root = [-1, -1]
        max_bit = max(nums).bit_length()

        for num in nums:
            buildTrie(root, num, max_bit)

        result = 0 

        for num in nums:
            cur = root
            xor_value = 0
            bits = bin(num)[2:].zfill(max_bit)

            for ch in bits:
                bit = int(ch)
                wanted = 1- bit

                if cur[wanted] != -1:
                    xor_value = xor_value * 2 + 1
                    cur = cur[wanted]
                else:
                    xor_value = xor_value * 2
                    cur = cur[bit]

            result = max(result, xor_value)

        return result