class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        
        q = deque([source])
        visited = set()

        while q:
            vertex = q.popleft()
            if vertex == destination:
                return True

            visited.add(vertex)
            
            for v in adj[vertex]:
                if v not in visited:
                    q.append(v)
        
        return False

        