class Solution:
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])
        vis = set()

        def dfs(i, j):
            vis.add((i, j))
            count = 1

            for y in range(n):
                if grid[i][y] == 1 and (i, y) not in vis:
                    count += dfs(i, y)

            for x in range(m):
                if grid[x][j] == 1 and (x, j) not in vis:
                    count += dfs(x, j)

            return count

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in vis:
                    cnt = dfs(i, j)

                    if cnt > 1:
                        ans += cnt

        return ans