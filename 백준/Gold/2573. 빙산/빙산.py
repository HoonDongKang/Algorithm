import sys
from collections import deque

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def divided_bfs(n: int, m: int, field: list[list[int]], visited: list[list[bool]]):
    count = 0

    def bfs(x: int, y:int):
        queue = deque([(x,y)])
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx,ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

    for x in range(n):
        for y in range(m):
            if field[x][y] > 0 and not visited[x][y]:
                bfs(x,y)
                count += 1

    return count

def solve(n: int, m: int, field: list[list[int]]):
    icebergs = deque()
    year = 0

    for x in range(n):
        for y in range(m):
            if field[x][y] > 0:
                icebergs.append((x, y))

    while icebergs:
        visited = [[False] * m for _ in range(n)]
        melts = [0] * len(icebergs)
        new_icebergs = deque()

        if divided_bfs(n,m,field,visited) > 1:
            return year

        for i, (x,y) in enumerate(icebergs):
            sea = 0
            for dx, dy in DIRECTIONS:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
                    sea += 1
            
            melts[i] = sea

        for i, (x,y) in enumerate(icebergs):
            field[x][y] = max(0, field[x][y] - melts[i])
            if field[x][y] > 0:
                new_icebergs.append((x,y))

        icebergs = new_icebergs
        year += 1

    return 0 

def main():
    n, m = map(int, sys_input().split())
    field = [list(map(int, sys_input().split())) for _ in range(n)]

    print(solve(n, m, field))

if __name__ == "__main__":
    main()
