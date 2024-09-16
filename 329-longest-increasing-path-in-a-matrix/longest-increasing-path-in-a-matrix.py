class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = set()
        ans = 0
        @cache
        def dfs(r, c, prev):
            if min(r, c) < 0 or r >= len(matrix) or c >= len(matrix[0]) or (r, c) in visited:
                return 0
            
            if matrix[r][c] <= prev:
                return 0
            
            visited.add((r, c))

            res = 0
            res = max(res, 1 +dfs(r + 1, c, matrix[r][c])) 
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            visited.remove((r, c))
            return res


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j, -1))

        return ans