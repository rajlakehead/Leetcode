class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, lst):
            nonlocal res
            if len(lst) == k:
                res.append(lst.copy())
                return
            if i > n:
                return

            lst.append(i)
            dfs(i + 1, lst)

            lst.remove(i)
            dfs(i + 1, lst)
        dfs(1, [])
        return res


        