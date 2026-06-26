import heapq
class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for _ in range(n)]
        rev_graph = [[] for _ in range(n)]

        src1_distance = [float('inf')] * n
        src1_distance[src1] = 0
        src1_heap = [(0, src1)]

        src2_distance = [float('inf')] * n
        src2_distance[src2] = 0
        src2_heap = [(0, src2)]

        dest_distance = [float('inf')] * n
        dest_distance[dest] = 0
        dest_heap = [(0, dest)]

        for a,b,c, in edges:
            graph[a].append((b,c))
            
        for a,b,c, in edges:
            rev_graph[b].append((a,c))

        def dijkstra(heap, distance, graph):
            while heap:
                cur_cost, next_node = heapq.heappop(heap)

                if cur_cost > distance[next_node]:
                    continue

                for edge, cost in graph[next_node]:
                    next_cost = cur_cost + cost

                    if next_cost <= distance[edge]:
                        distance[edge] = next_cost
                        heapq.heappush(heap, (next_cost, edge))

            return distance
        
        src1_distance = dijkstra(src1_heap, src1_distance, graph)
        src2_distance = dijkstra(src2_heap, src2_distance, graph)
        dest_distance = dijkstra(dest_heap, dest_distance, rev_graph)

        answer = float('inf')

        for mid in range(n):
            if src1_distance[mid] == float("inf"):
                continue
            if src2_distance[mid] == float("inf"):
                continue
            if dest_distance[mid] == float("inf"):
                continue

            
            answer = min(
                answer,
                src1_distance[mid] + src2_distance[mid] + dest_distance[mid]
            )

        if answer == float("inf"):
            return -1

        return answer