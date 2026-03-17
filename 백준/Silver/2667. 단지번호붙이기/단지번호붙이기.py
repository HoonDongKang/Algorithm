import sys
from collections import deque

DIRECTION = [(1,0),(-1,0),(0,1),(0,-1)]

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n, field):
    visited = [[False]*n for _ in range(n)]
    components = []

    for y in range(n):
        for x in range(n):
            if field[y][x] == 1 and not visited[y][x]:
                queue = deque([(x,y)])
                visited[y][x] = True
                count = 1

                while queue:
                    cx, cy = queue.popleft()

                    for dx, dy in DIRECTION:
                        nx, ny = cx + dx, cy + dy

                        if 0<=nx<n and 0<=ny<n and field[ny][nx]==1 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((nx,ny))
                            count += 1

                components.append(count)

    return sorted(components)

def main():
    n = int(sys_input())
    field = [list(map(int, sys_input().strip())) for _ in range(n)]

    answers = solve(n, field)

    print(len(answers))
    for a in answers:
        print(a)

if __name__ == "__main__":
    main()