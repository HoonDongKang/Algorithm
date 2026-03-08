import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def fire_bfs(m: int, n:int, field: list[list[str]]):
    queue = deque()
    fire_time = [[-1] * m for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for x in range(n):
        for y in range(m):
            if field[x][y] == '*':
                queue.append((x,y))
                fire_time[x][y] = 0    


    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and fire_time[nx][ny] == -1 and field[nx][ny] != '#':
                fire_time[nx][ny] = fire_time[x][y] +1
                queue.append((nx,ny))
        
    return fire_time

def human_bfs(m: int, n:int, field: list[list[str]], fire_time: list[list[int]]):
    queue = deque()
    human_time = [[-1]*m for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for x in range(n):
        for y in range(m):
            if field[x][y] == '@':
                queue.append((x,y))
                human_time[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            nt = human_time[x][y] + 1

            if ny < 0 or ny >= m or nx < 0 or nx >= n:
                return human_time[x][y] + 1
            
            if 0 <= nx < n and 0 <= ny < m \
                and human_time[nx][ny] == -1 \
                and field[nx][ny] != '#' \
                and (fire_time[nx][ny] == -1 or nt < fire_time[nx][ny]):
                human_time[nx][ny] = human_time[x][y] + 1
                queue.append((nx,ny))

    return 'IMPOSSIBLE'

def solve(m: int, n:int, field: list[list[str]]):
    fire_time = fire_bfs(m,n,field)
    count = human_bfs(m, n, field, fire_time)

    return count

def main():
    length = int(sys_input())
    result = []

    for _ in range(length):
        m, n,  = map(int, sys_input().split())
        field = [list(sys_input()) for _ in range(n)]
        result.append(solve(m, n, field))

    for answer in result:
        print(answer)

if __name__ == "__main__":
    main()
