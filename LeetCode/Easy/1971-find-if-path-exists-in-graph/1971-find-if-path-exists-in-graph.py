from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        queue = deque([source])
        visited = [False] * n
        graph = [[] for _ in range(n)]

        if source == destination:
            return True

        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited[source] = True

        while queue:
            node = queue.popleft()

            for edge in graph[node]:
                if edge == destination:
                    return True
                
                if visited[edge]:
                    continue

                queue.append(edge)
                visited[edge] = True
            
        return False
        