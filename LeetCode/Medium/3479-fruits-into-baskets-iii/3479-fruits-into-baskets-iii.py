class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        tree = [0] * (len(baskets) * 4)

        def buildTree(node, start, end):
            if start == end:
                tree[node] = baskets[start]
                return
            
            mid = (start + end) // 2 
            
            buildTree(node * 2, start, mid)
            buildTree(node * 2 + 1, mid + 1, end)

            tree[node] = max(tree[node * 2], tree[node * 2 + 1])
            
        def findAndUse(node, start, end, fruit):
            if tree[node] < fruit:
                return False
            
            if start == end:
                tree[node] = 0
                return True
            
            mid = (start + end) // 2

            if tree[node * 2] >= fruit:
                used = findAndUse(node*2, start, mid, fruit)
            else:
                used = findAndUse(node*2+1, mid + 1, end, fruit)

            tree[node] = max(tree[node*2], tree[node*2+1])

            return used
     
        unplaced = 0
        buildTree(1, 0, len(baskets) - 1)

        for fruit in fruits:
            if not findAndUse(1, 0, len(baskets) - 1, fruit):
                unplaced+=1

        return unplaced