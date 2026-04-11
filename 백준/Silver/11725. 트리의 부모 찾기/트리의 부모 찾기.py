import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, n_list:list[int]):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    parent = [0] * (n+1)
    queue = deque([1])
    visited[1] = True

    for u,v in n_list:
        graph[u].append(v)
        graph[v].append(u)

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                parent[next_node] = node
                visited[next_node] = True
                queue.append(next_node)
    return parent
    

def main():
    n = int(sys_input())
    n_list = [tuple(map(int, sys_input().split())) for _ in range(n-1)]
    answers = solve(n,n_list)
    for i in range(2, n+1):
        print(answers[i])

if __name__ == "__main__":
    main()
