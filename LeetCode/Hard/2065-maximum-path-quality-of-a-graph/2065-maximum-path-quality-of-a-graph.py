class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        graph = [[] for _ in range(len(values) + 1)]
        visited = [False for _ in range(len(values) + 1)]
        result = 0

        for a,b,c, in edges:
            graph[a].append((b,c))
            graph[b].append((a,c))


        def dfs(cur_node, cur_time, cur_value):
            nonlocal result
            nodes = graph[cur_node]

            if cur_node == 0:
                value = 0
                if not visited[0]:
                    value = values[0]                    
                result = max(result, cur_value + value)
            
            for node in nodes:
                next_node, time = node
                next_value = values[next_node]

                if cur_time + time <= maxTime:
                    if not visited[next_node]:
                        visited[next_node] = True
                        dfs(next_node, cur_time + time, cur_value + next_value)
                        visited[next_node] = False
                    else:
                        dfs(next_node, cur_time + time, cur_value)

        visited[0] = True
        dfs(0, 0, values[0])

        return result