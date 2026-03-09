import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(N: int, M:int, field: list[list[str]]):
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0,0,0,1)])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited[0][0][0] = True
    while queue:
        x, y, is_break, dist = queue.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if x == N-1 and y == M-1:
                return dist
            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == '0' and not visited[nx][ny][is_break]:
                    visited[nx][ny][is_break] = True
                    queue.append((nx, ny, is_break, dist+1))
                elif field[nx][ny] == '1' and is_break == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx,ny,1, dist + 1))
    
    return -1

def main():
    N, M = map(int, sys_input().split())
    field = [list(sys_input()) for _ in range(N)]

    answer = solve(N, M, field)
    print(answer)

if __name__ == "__main__":
    main()
