class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid1) or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            
            grid2[r][c] = 0

            res = grid1[r][c] == 1

            res &= dfs(r + 1, c)
            res &= dfs(r, c + 1) 
            res &= dfs(r - 1, c)
            res &= dfs(r, c - 1)

            return res
        
        res = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and dfs(i, j):
                    res += 1
        return res