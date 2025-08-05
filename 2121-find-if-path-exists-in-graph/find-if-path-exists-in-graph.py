class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        
        def dfs(node):
            if node in visited:
                return False

            if node == destination:
                return True
            
            visited.add(node)
            for neighbour in adj[node]:
                if dfs(neighbour):
                    return True
            return False

        return dfs(source)

        