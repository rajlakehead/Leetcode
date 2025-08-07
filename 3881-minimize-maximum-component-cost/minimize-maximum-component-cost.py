class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if not edges:
            return 0
   
        def canFormKComponents(maxEdge):
            parent = list(range(n))

            def find(x):
                while x != parent[x]:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            
            def union(x, y):
                rootX, rootY = find(x), find(y)
                if rootX != rootY:
                    parent[rootY] = rootX
                    return True
                return False

            components = n
            for u, v, w in edges:
                if w <= maxEdge and union(u, v):
                    components -= 1
            return components <= k

        left, right = 0, max(w for _, _, w in edges)
        res = right

        while left < right:
            mid = (left + right) // 2
            if canFormKComponents(mid):
                res = mid
                right = mid
            else:
                left = mid + 1

        return left
