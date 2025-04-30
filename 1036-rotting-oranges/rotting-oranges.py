class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        while q and fresh:

            for i in range(len(q)):
                row, col = q.popleft()

                for r, c in directions:
                    if r + row < 0 or c + col < 0 or r + row >= len(grid) or c + col >= len(grid[0]):
                        continue
                    if grid[r + row][c + col] == 0 or grid[r + row][c + col] == 2:
                        continue
                    
                    grid[r + row][c + col] = 0
                    fresh -= 1
                    q.append((r + row, c + col))
            time += 1
            
        return time if fresh == 0 else -1