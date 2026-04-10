import sys
from collections import deque

DIRECTION = [(1,0), (-1,0), (0,1), (0,-1)]

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, m:int, tomatos:list[list[int]]):
    dist = [[0] * m for _ in range(n)]
    start= []
    max_day = 0

    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 1:
                start.append((i,j))

    queue = deque(start)

    while queue:
        x,y = queue.popleft()
        for dx, dy in DIRECTION:
            nx,ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m:
                if tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 0:
                return -1
            max_day = max(max_day, dist[i][j])

    return max_day


def main():
    m,n = map(int, sys_input().split())
    tomatos = [list(map(int, sys_input().split())) for _ in range(n)]

    answer = solve(n,m,tomatos)
    print(answer)

if __name__ == "__main__":
    main()
