class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= n or c >= n or grid[r][c] == 0:
                return

            q.append((r, c))
            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)


        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    visited.add((i, j))
                    found = True
                    break
        
        res = 0
        while q:
            
            for i in range(len(q)):
                points = q.popleft()

                row, col = points[0], points[1]
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                

                for dr, dc in directions:
                    if (row + dr) < 0 or (col + dc) < 0 or (row + dr) >= n or (col + dc) >= n:
                        continue
                    
                    if (row + dr, col + dc) in visited:
                        continue
                    
                    if grid[row + dr][col + dc] == 1:
                        return res

                    visited.add((row + dr, col + dc))
                    q.append((row + dr, col + dc))
            res += 1


                


        