import heapq
class Graph:
    graph = []
    n = 0
    def __init__(self, n: int, edges: list[list[int]]):
        
        self.graph = [[] for _ in range(n)]
        self.n = n

        for a,b,c in edges:
            self.graph[a].append((b,c))

    def addEdge(self, edge: list[int]) -> None:
        a,b,c = edge

        self.n = self.n + 1
        self.graph[a].append((b,c))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        distance = [float("inf")] * self.n
        distance[node1] = 0
        heap = [(0, node1)]

        while heap:
            cur_cost, next_node = heapq.heappop(heap)

            if cur_cost > distance[next_node]:
                continue

            if next_node == node2:
                return cur_cost

            for edge, cost in self.graph[next_node]:
                next_cost = cost + cur_cost

                if next_cost <= distance[edge]:
                    distance[edge] = next_cost
                    heapq.heappush(heap, (next_cost, edge))

        return -1