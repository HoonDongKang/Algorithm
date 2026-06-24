from collections import deque
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * (n)
        queue = deque([])
        components= []
        result = 0

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for start in range(n):
            if visited[start]:
                continue

            queue = deque([start])
            visited[start] = True

            component= []

            while queue:
                node = queue.popleft()
                component.append(node)
                for next_node in graph[node]:
                    if visited[next_node]:
                        continue

                    visited[next_node] = True
                    queue.append(next_node)

            components.append(component)

        for component in components:
            total = 0
            k = len(component)
            for node in component:
                total += len(graph[node])

            if total == k *(k-1):
                result += 1

        return result