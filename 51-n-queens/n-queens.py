class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diagonal = set()
        d = set()

        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(i):
            if i >= n:
                temp = []
                for l in board:
                    temp.append(''.join(l))
                res.append(temp)

                return

            for j in range(n):
                if j not in cols and i + j not in diagonal and i - j not in d:
                    board[i][j] = "Q"
                    cols.add(j)
                    diagonal.add(i + j)
                    d.add(i - j)

                    dfs(i + 1)

                    board[i][j] = "."
                    cols.remove(j)
                    diagonal.remove(i + j)
                    d.remove(i - j)
        dfs(0)
        return res
                    




