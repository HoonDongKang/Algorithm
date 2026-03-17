import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(jump_count:int, n:int, m:int, field:list[list[int]]) -> int:
    dist = [[[-1]*(jump_count+1) for _ in range(n)] for _ in range(m)]

    horse_directon = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    monkey_direction = [(1,0), (-1, 0), (0, 1), (0,-1)]

    queue = deque([(0,0,0)])
    dist[0][0][0] = 0

    while queue:
        x, y, jump = queue.popleft()

        if x == n-1 and y == m-1:
            return dist[y][x][jump]

        for dx, dy in monkey_direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and field[ny][nx] != 1 and dist[ny][nx][jump] == -1:
                dist[ny][nx][jump] = dist[y][x][jump] + 1
                queue.append((nx, ny, jump))

        if jump >= jump_count:
            continue

        for dx, dy in horse_directon:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and field[ny][nx] != 1 and dist[ny][nx][jump+1] == -1:
                dist[ny][nx][jump+1] = dist[y][x][jump] + 1
                queue.append((nx, ny, jump+1))

    return -1
def main():
    jump_count = int(sys_input())
    n, m = map(int, sys_input().split())
    field = [list(map(int, sys_input().split())) for _ in range(m)]

    answer = solve(jump_count, n, m, field)
    print(answer)

if __name__ == "__main__":
    main()
