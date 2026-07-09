class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        index_edges = []

        for i, (a, b, weight) in enumerate(edges):
            index_edges.append((a, b, weight, i))

        index_edges.sort(key=lambda x: x[2])

        def kruskal(skip_index=-1, force_edge=None):
            parent = [i for i in range(n)]

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(a, b):
                root_a = find(a)
                root_b = find(b)

                if root_a == root_b:
                    return False

                parent[root_b] = root_a
                return True
            
            cost = 0
            edge_count = 0
            
            if force_edge:
                a, b, weight, original_index = force_edge
                union(a, b)
                cost += weight
                edge_count += 1
                

            for a, b, weight, original_index in index_edges:
                if original_index == skip_index:
                    continue

                if force_edge and original_index == force_edge[3]:
                    continue
                
                if union(a,b):
                    cost += weight
                    edge_count += 1

                    if edge_count == n - 1:
                        break
            
            if edge_count != n - 1:
                return float('inf')
            
            return cost
        
        base_cost = kruskal()
        critical = []
        pseudo_critical = []

        for a, b, weight, original_index in index_edges:
            tmp_cost = kruskal(skip_index=original_index)

            if tmp_cost > base_cost:
                critical.append(original_index)
                continue

            forced_cost = kruskal(force_edge=(a, b, weight, original_index))

            if forced_cost == base_cost:
                pseudo_critical.append(original_index)

        return [critical, pseudo_critical]

