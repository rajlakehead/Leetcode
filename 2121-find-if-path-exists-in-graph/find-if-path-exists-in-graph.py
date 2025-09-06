class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(s):
            if s in visited:
                return False
            
            if s == destination:
                return True
            
            visited.add(s)

            for nei in adj[s]:
                if dfs(nei):
                    return True
            return False
        return dfs(source)