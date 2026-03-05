import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(M:int, N:int, field, visited, node):
    queue = deque([node])
    visited[node[0]][node[1]] = True

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            update_x = dx + x
            update_y = dy + y
            if 0 <= update_x < N and 0 <= update_y < M and field[update_x][update_y] == 1 and not visited[update_x][update_y]:
                visited[update_x][update_y] = True
                queue.append((update_x, update_y))

def solve(M: int, N:int, cabbage_locations: list[tuple[int,int]]) -> int:
    count = 0
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for x, y in cabbage_locations:
        field[y][x] = 1

    for x, y in cabbage_locations:
        if not visited[y][x]:
            bfs(M, N, field, visited, (y,x))
            count += 1


    return count

def main() -> None:
    answers = []
    length = int(sys_input())

    for _ in range(length):
        M, N, cabbage_count = map(int, sys_input().split())
        cabbage_locations = []

        for _ in range(cabbage_count):
            x, y = map(int, sys_input().split())
            cabbage_locations.append((x, y))

        warm_count = solve(M, N, cabbage_locations)
        answers.append(warm_count)

    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
