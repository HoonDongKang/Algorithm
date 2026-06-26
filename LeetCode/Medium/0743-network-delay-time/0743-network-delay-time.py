import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        distance = [float('inf')] * (n+1)
        
        heap = [(0, k)]
        distance[k] = 0

        for a,b,c in times:
            graph[a].append((c, b))

        while heap:
            cur_cost, node = heapq.heappop(heap)
            if cur_cost > distance[node]:
                continue

            for edge_cost, edge in graph[node]:
                new_cost = cur_cost + edge_cost

                if new_cost < distance[edge]:
                    distance[edge] = new_cost
                    heapq.heappush(heap, (new_cost, edge))

        for dist in distance[1:]:
            if dist == float('inf'):
                return -1
        
        return max(distance[1:])