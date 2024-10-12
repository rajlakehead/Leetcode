pref = []

class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.pref = matrix
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                self.pref[i][j] += self.pref[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += (self.pref[i][col2] - (self.pref[i][col1-1] if col1 != 0 else 0))
        return ans