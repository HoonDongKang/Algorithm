import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(node, field, visited, is_rg):
    queue = deque([node])
    x, y = node
    visited[x][y] = True
    N = len(field)
    color = field[x][y]

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                next_color = field[nx][ny]

                if not is_rg:
                    if next_color == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if (color in {'R','G'} and next_color in {'R','G'}) or next_color == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))


def solve(field, is_rg):
    N = len(field)
    visited = [[False]*N for _ in range(N)]
    count = 0

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                bfs((x,y), field, visited, is_rg)
                count += 1

    return count


def main():
    N = int(sys_input())
    field = [list(sys_input()) for _ in range(N)]

    normal = solve(field, False)
    rg = solve(field, True)

    print(normal, rg)


if __name__ == "__main__":
    main()
