import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, m:int, r:int, vertexes:list[tuple[int,int]]):
    visited = [False] * (n+1)
    graph = [[] for _ in range(n + 1)]
    queue = deque([r])
    visited[r] = True
    cnt = 1
    result = [0] * (n + 1)
    result[r] = cnt

    for u,v in vertexes:
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        graph[i].sort()

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                cnt += 1
                result[next_node]= cnt
                queue.append(next_node)

    return result

def main():
    n,m,r = map(int, sys_input().split())
    vertexes = [tuple(map(int, sys_input().split())) for _ in range(m)]

    answers = solve(n,m,r, vertexes)

    for i in range(1, n+1):
        print(answers[i])

if __name__ == "__main__":
    main()
