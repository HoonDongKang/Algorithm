from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        queue = deque([(0, [0])])
        destination = len(graph) - 1
        result = []
        
        while queue:
            node, cur_path = queue.popleft()
            print(node, cur_path)

            for edge in graph[node]:
                new_path = cur_path + [edge]
                if edge == destination:
                    result.append(new_path)
                else:
                    queue.append((edge,new_path))
                    
        return result