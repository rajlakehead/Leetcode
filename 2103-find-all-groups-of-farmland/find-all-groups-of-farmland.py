class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        r2, c2 = 0, 0
        def dfs(r, c):
            nonlocal r2, c2
            if r < 0 or c < 0 or r > len(land) - 1 or c > len(land[0]) - 1:
                return
            
            if land[r][c] == 0:
                return
            
            land[r][c] = 0

            if r >= r2:
                r2 = r
                c2 = c

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    r2, c2 = i, j
                    dfs(i, j)
                    res.append([i, j, r2, c2])
        
        return res

        