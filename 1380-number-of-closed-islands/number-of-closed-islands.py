class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols:
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return up and down and left and right
        c=0
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if grid[i][j]==0:
                    if dfs(i,j):
                        c+=1
        return c