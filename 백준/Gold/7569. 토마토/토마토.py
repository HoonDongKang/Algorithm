import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(m: int, n:int, h: int, field: list[list[int]]):
    count = 0
    queue = deque()
    directions =  [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if field[z][x][y] == 1:
                    queue.append((z,x,y))

    while queue:
        z,x,y = queue.popleft()

        for dz, dx, dy in directions:
            update_z, update_x, update_y = dz+z, dx+x, dy+y
            if 0<=update_z<h and 0<=update_x<n and 0<=update_y<m and field[update_z][update_x][update_y] == 0:
                field[update_z][update_x][update_y] = field[z][x][y] + 1
                queue.append((update_z,update_x,update_y))

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if field[z][x][y] == 0:
                    return -1
                count = max(count, field[z][x][y])
            
    return count - 1


def main():
    m, n, h = map(int, sys_input().split())
    field = [[[*map(int, sys_input().split())] for _ in range(n)] for _ in range(h)]
    answer = solve(m,n,h,field)

    print(answer)


if __name__ == "__main__":
    main()
