from collections import deque
class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        queue = deque([1])
        visited = [False] * (n+1)
        visited[1] = True
        graph = [[] for _ in range(n+1)]
        result = float("inf") 

        for a,b,c in roads:
            graph[a].append((b,c))
            graph[b].append((a,c))

        while queue:
            node = queue.popleft()
            for edge, point in graph[node]:
                result = min(point, result)

                if visited[edge]:
                    continue

                visited[edge] = True
                queue.append(edge)

        return result
