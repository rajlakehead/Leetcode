class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        res = -1

        def dfs(node, dist, step):
            nonlocal res
            visited.add(node)
            dist[node] = step

            neighbor = edges[node]
            if neighbor != -1:
                if neighbor not in visited:
                    dfs(neighbor, dist, step + 1)
                elif neighbor in dist:
                    # Found a cycle, calculate its length
                    res = max(res, step - dist[neighbor] + 1)

            dist.pop(node)  # remove from current recursion stack

        for i in range(n):
            if i not in visited:
                dfs(i, {}, 1)
        return res
