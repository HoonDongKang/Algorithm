from collections import deque
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        DIRECTION = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque([])
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        result = 0

        start = None

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i, j)
                    break

            if start is not None:
                break

        if start is None:
            return 0
        
        queue.append(start)
        visited[start[0]][start[1]] = True

        while queue:
            x,y = queue.popleft()

            for dx, dy in DIRECTION:
                nx = dx + x
                ny = dy + y
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    result += 1
                    continue

                if grid[nx][ny] == 0:
                    result += 1
                    continue

                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
            
        return result