import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def dfs(N: int, M:int, V:int, graph: list[list[int]]):
    visited = [False for _ in range(N+1)]
    result = []
    stack = [V]

    while stack:
        node = stack.pop()
        if not visited[node]:
            result.append(node)
            visited[node] = True
            
            for nn in reversed(graph[node]):
                if not visited[nn]:
                    stack.append(nn)
        
    return result

def bfs(N: int, M:int, V:int, graph: list[list[int]]):
    visited = [False for _ in range(N+1)]
    result = []
    queue = deque([V])
    visited[V] = True

    while queue:
        node = queue.popleft()
        result.append(node)
        
        for nn in graph[node]:
            if not visited[nn]:
                visited[nn] = True
                queue.append(nn)
    
    return result

def solve(N: int, M:int, V:int, node: list[tuple[int,int]]):
    graph = [[] for _ in range(N+1)]
    
    for i in range(M):
        a, b =  node[i]
        graph[a].append(b)
        graph[b].append(a)
    
    for node in graph:
        node.sort()

    dfs_visit = dfs(N, M, V, graph)
    bfs_visit = bfs(N, M, V, graph)

    print(*dfs_visit)
    print(*bfs_visit)

def main():
    N, M, V= map(int, sys_input().split())
    node = [tuple(map(int, sys_input().split())) for _ in range(M)]

    solve(N, M, V, node)

if __name__ == "__main__":
    main()
