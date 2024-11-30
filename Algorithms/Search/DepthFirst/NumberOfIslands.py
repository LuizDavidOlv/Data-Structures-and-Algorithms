# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class SolutionDfsMutable:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(self, i,j, rows,cols):
            if i < 0 or i >= rows or j<0 or j >= cols or grid[i][j] != '1':
                return
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1) 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i,j)

        return count




class SolutionDfsImmutable:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i,j):
            if i<0 or j<0 or i>= rows or j >= cols or grid[i][j] != '1' or visited[i][j]:
                return
            
            visited[i][j] =True

            dfs(i-1,j) #up
            dfs(i+1,j) #down
            dfs(i,j-1) #left
            dfs(i,j+1) #right


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i,j)

        return count

