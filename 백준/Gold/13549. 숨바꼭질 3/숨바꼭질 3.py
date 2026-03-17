import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(n: int, k: int):
    dist = [-1] * 100001
    queue = deque([n])
    dist[n] = 0

    while queue:
        node = queue.popleft()

        if node == k:
            return dist[node]

        for nx in (node*2, node-1, node+1):
            if 0 <= nx <= 100000 and dist[nx] == -1:
                if nx == 2*node:
                    dist[nx] = dist[node]
                    queue.appendleft(nx)
                else:
                    dist[nx] = dist[node] + 1
                    queue.append(nx)

    return 0


def main():
    n, k = map(int, sys_input().split())

    d = solve(n, k)

    print(d)

if __name__ == "__main__":
    main()
