class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                total += grid[r][c]
            
        
        if total % 2 != 0:
            return False
        
        curr = 0
        for r in range(len(grid)):
            curr += sum(grid[r])
            if curr * 2 == total:
                return True

        curr = 0
        for c in range(len(grid[0]) - 1):
            for r in range(len(grid)):
                curr += grid[r][c]
            
            if curr * 2 == total:
                return True
        return False

