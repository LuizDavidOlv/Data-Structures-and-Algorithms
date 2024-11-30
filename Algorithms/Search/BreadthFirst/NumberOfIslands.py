from collections import deque
from typing import List


class SolutionMutable:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0),(  1,0),(0,-1),(0,1)]

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            grid[i][j] = '0'

            while queue:
                x,y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < rows and 0  <= new_y < cols and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] == '0'
                        queue.append((new_x,new_y))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i,j)

        return count

class SolutionImutable:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True

            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    new_x, new_y = x +dx, y+dy
                    if 0 <= new_x < rows and 0  <= new_y < cols and grid[new_x][new_y] == '1' and not visited[new_x][new_y]:
                        visited[new_x][new_y] = True
                        queue.append((new_x,new_y))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    bfs(i,j)
        
        return count
        
