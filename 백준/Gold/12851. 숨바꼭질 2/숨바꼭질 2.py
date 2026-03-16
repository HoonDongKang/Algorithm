import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(n: int, k: int):
    dist = [[-1, 0] for _ in range(100001)]
    dist[n] = [0, 1]

    queue = deque([n])

    while queue:
        node = queue.popleft()

        for nx in (node-1, node+1, node*2):
            if 0 <= nx <= 100000:

                if dist[nx][0] == -1:
                    dist[nx][0] = dist[node][0] + 1
                    dist[nx][1] = dist[node][1]
                    queue.append(nx)

                elif dist[nx][0] == dist[node][0] + 1:
                    dist[nx][1] += dist[node][1]

    return dist[k]

def main():
    n, k = map(int, sys_input().split())

    d, count = solve(n, k)

    print(d)
    print(count)

if __name__ == "__main__":
    main()
