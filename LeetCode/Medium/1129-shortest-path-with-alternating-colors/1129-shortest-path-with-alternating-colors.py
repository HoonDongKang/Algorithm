from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        red_graph = [[] for _ in range(n)]
        blue_graph = [[] for _ in range(n)]

        red_visited = [False] * n
        blue_visited = [False] * n

        red_visited[0] = True
        blue_visited[0] = True

        queue = deque([
            (0, 0, "red"),
            (0, 0, "blue")
        ])

        result = [-1] * n
        result[0] = 0

        for a,b in redEdges:
            red_graph[a].append(b)
        for a,b in blueEdges:
            blue_graph[a].append(b)

        while queue:
            node, count, color = queue.popleft()

            if color == 'red':
                for edge in blue_graph[node]:
                    if blue_visited[edge]:
                        continue
                    blue_visited[edge] = True

                    if result[edge] == -1:
                        result[edge] = count + 1
                    queue.append((edge, count + 1, 'blue'))

            if color == 'blue':
                for edge in red_graph[node]:
                    if red_visited[edge]:
                        continue
                    red_visited[edge] = True

                    if result[edge] == -1:
                        result[edge] = count + 1
                        
                    queue.append((edge, count + 1, 'red'))

        return result