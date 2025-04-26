class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = [0] * len(graph)  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res