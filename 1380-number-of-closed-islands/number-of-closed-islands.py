class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n,res = len(grid),len(grid[0]),0
        def dfs(i,j):
            nonlocal grid 
            if(i<0 or j<0 or i>=m or j>=n ):
                return False 
            elif(grid[i][j] == 1):
                return True
            grid[i][j] = 1
            ans = True 
            ans = dfs(i+1,j) and ans 
            ans = dfs(i-1,j) and ans 
            ans = dfs(i,j+1) and ans 
            ans = dfs(i,j-1) and ans 
            return ans
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j] != 1 and  dfs(i,j)):
                    res += 1
        return res  