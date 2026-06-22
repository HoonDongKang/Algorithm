class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parent = {}
        size = {}

        def find(x:int):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]
        
        def union(a:int, b:int):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return
            
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        for num in nums:
            parent[num] = num
            size[num] = 1

        for num in parent:
            if num+1 in parent:
                union(num, num+1)

        return max(size.values())