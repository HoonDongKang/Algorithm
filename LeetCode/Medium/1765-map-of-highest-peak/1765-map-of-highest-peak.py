from collections import deque
class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)]
        row = len(isWater)
        col = len(isWater[0])
        answer = [[-1 for _ in range(col)] for _ in range(row)]
        visited = [[False for _ in range(col)] for _ in range(row)]
        queue = deque()

        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    answer[i][j] = 0
                    queue.append((i,j))
                    visited[i][j] = True

        while queue:
            x,y = queue.popleft()
            cur_height = answer[x][y]

            for dx, dy in DIRECTION:
                nx = dx + x
                ny = dy + y

                if nx >= 0 and nx < row and ny >=0 and ny < col:
                    if not visited[nx][ny]:
                        answer[nx][ny] = cur_height + 1
                        queue.append((nx,ny))
                        visited[nx][ny] = True

        return answer