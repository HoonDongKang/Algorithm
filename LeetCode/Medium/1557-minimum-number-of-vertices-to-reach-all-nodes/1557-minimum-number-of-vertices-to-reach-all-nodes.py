class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes= {}
        result = []

        for a,b in edges:
            if not a in nodes:
                nodes[a] = 0

            if not b in nodes:
                nodes[b] = 0

            nodes[b] += 1

        for node in nodes.keys():
            if not nodes[node]:
                result.append(node)

        return result