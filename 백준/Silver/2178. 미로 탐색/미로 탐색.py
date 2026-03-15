import sys
from collections import deque

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(n: int, m: int, field: list[list[int]]):
    queue = deque([(0,0)])
    dist = [[0]*m for _ in range(n)]
    dist[0][0] = 1
    
    while queue:
        x,y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = dx + x, dy + y
            if 0<= nx < n and 0<= ny < m and field[nx][ny] ==1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist[n-1][m-1]

def main():
    n, m = map(int, sys_input().split())
    field = [list(map(int, sys_input())) for _ in range(n)]

    print(solve(n, m, field))

if __name__ == "__main__":
    main()
