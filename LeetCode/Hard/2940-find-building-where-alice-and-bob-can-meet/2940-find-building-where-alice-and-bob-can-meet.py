class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        length = len(heights)
        tree = [0] * (4 * length)
        result = []

        def build(node, start, end):
            if start == end:
                tree[node] = heights[start]
                return
            
            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, length - 1)

        def findLeftMost(node, start, end, index, val):
            if end < index:
                return -1
            
            if tree[node] <= val:
                return -1
            
            if start == end:
                return start
            
            mid =(start + end) // 2
            
            left_most =  findLeftMost(node*2, start, mid, index, val)
            if left_most == -1:
                return findLeftMost(node * 2 + 1, mid + 1, end, index,val)
            
            return left_most

        def query(a, b):
            if a == b:
                return a
            
            left = min(a,b)
            right = max(a,b)

            if heights[left] < heights[right]:
                return right

            start = right + 1
            height = max(heights[a], heights[b])

            return findLeftMost(1, 0, length - 1, start, height)

        for [a,b] in queries:
            building = query(a, b)
            result.append(building)

        return result