class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        odd_degrees = []

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for node, degree in enumerate(graph):
            if len(degree) % 2 != 0:
                odd_degrees.append(node)

        if len(odd_degrees) > 4:
            return False
        
        if len(odd_degrees) == 0:
            return True
        
        if len(odd_degrees) == 2:
            a, b = odd_degrees
            a_degree = graph[a]
            b_degree = graph[b]

            if not b in a_degree and not a in b_degree:
                return True
            
            for x in range(1,n+1):
                if x == a or x == b:
                    continue
                if x in graph[a] or x in graph[b]:
                    continue
                
                return True
            
            return False
        
        if len(odd_degrees) == 4:
            x, y, z, i = odd_degrees
            

            cases = [
                ((x, y), (z, i)),
                ((x, z), (y, i)),
                ((x, i), (y, z)),
            ]

            for case in cases:
                a,b = case[0]
                c,d = case[1]

                if a not in graph[b] and c not in graph[d]:
                    return True

            return False 
        
        return False
