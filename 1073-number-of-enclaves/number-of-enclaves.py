class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        

        def dfs(r, c):
            if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == 0:
                return
            
            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        for row in range(1, m):
            for col in range(1, n):
                if grid[row][col] == 1:
                    res += 1
        return res