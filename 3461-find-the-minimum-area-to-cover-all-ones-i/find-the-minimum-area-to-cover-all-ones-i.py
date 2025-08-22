class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row, col = float('inf'), float('inf')
        mxr = 0
        mxc = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    col = min(col, j)
                    row = min(row, i)
                    mxr = max(mxr, i)
                    mxc = max(mxc, j)
        return (mxr - row + 1) * (mxc - col + 1)
        