class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        parent = {}
        size = {}

        def find_prime(n):
            factors = []
            d = 2
            while d * d <= n:
                if n % d == 0:
                    factors.append(d)
                
                    while n % d == 0:
                        n //= d

                d += 1

            if n > 1:
                factors.append(n)

            return factors
        
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])

            return parent[n]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return
            
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        for num in nums:
            parent[num] = num
            size[num] = 1


        for num in nums:
            prime_factors = find_prime(num)

            for factor in prime_factors:
                if factor not in parent:
                    parent[factor] = factor
                    size[factor] = 0

                union(num, factor)

        return max(size[find(num)] for num in nums)
