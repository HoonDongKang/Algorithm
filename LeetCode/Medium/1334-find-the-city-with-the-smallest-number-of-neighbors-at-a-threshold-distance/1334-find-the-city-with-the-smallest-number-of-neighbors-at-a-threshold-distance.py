import heapq
class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]

        for a,b,c in edges:
            graph[a].append((b,c))
            graph[b].append((a,c))

        def dijkstra(start):
            heap = [(0, start)]
            distance = [float('inf')] * n
            distance[start] = 0

            while heap:
                cur_cost, node = heapq.heappop(heap)

                if cur_cost > distance[node]:
                    continue

                for next_node, cost in graph[node]:
                    next_cost = cost + cur_cost

                    if next_cost < distance[next_node]:
                        distance[next_node] = next_cost
                        heapq.heappush(heap, (next_cost, next_node))

            return distance
        
        best_city = 0
        best_count = float("inf")
        
        for city in range(n):
            distance = dijkstra(city)
            reachable_count = 0

            for other_city, dis in enumerate(distance):
                if other_city == city:
                    continue
                if dis <= distanceThreshold:
                    reachable_count += 1

            if reachable_count < best_count:
                best_count = reachable_count
                best_city = city
            elif reachable_count == best_count and city > best_city:
                best_count = reachable_count
                best_city = city

        return best_city