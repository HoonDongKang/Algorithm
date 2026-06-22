class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        parent = {}
        size = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return
            
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        for num in requests:
            a,b = num
            parent[a] = a
            parent[b] = b
            size[a] = 1
            size[b] = 1

        for a,b in restrictions:
            parent[a] = a
            parent[b] = b
            size[a] = 1
            size[b] = 1

        res = []
        for a,b in requests:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                res.append(True)
                continue
            
            can_union = True
            for x,y in restrictions:
                root_x = find(x)
                root_y = find(y)

                if (root_a == root_x and root_b == root_y) or (root_a == root_y and root_b == root_x):
                    can_union = False
                    break
            
            if can_union:
                union(a,b)
                res.append(True)
            else:
                res.append(False)

        return res