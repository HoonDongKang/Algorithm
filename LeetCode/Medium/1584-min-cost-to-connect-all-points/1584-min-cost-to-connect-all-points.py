class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        edges.sort(key = lambda x: x[0])

        def kruskal():
            parents = [i for i in range(len(points))]

            def find(x):
                if x != parents[x]:
                    parents[x] = find(parents[x])
                return parents[x]
            
            def union(a,b):
                root_a = find(a)
                root_b = find(b)

                if root_a == root_b:
                    return False

                parents[root_b] = root_a
                return True

            cost = 0
            edge_count = 0

            for weight, a, b in edges:
                if union(a,b):
                    cost += weight
                    edge_count += 1

                    if edge_count == len(points) - 1:
                        break

            if edge_count != len(points) - 1:
                return float('inf')
                
            return cost
        
        return kruskal()