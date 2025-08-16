class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        minheap = [(0, 0)]
        dist = [float('inf')] * n
        adj = defaultdict(list)
        visited = set()

        for u, v, s, e in edges:
            adj[u].append((v, s, e))


        while minheap:
            t, node = heapq.heappop(minheap)

            if node == n - 1:
                return t

            if node in visited:
                continue
            
            dist[node] = time
            visited.add(node)

            for dest, start, end in adj[node]:
                if t <= end:
                    newt = max(start, t)
                    heapq.heappush(minheap, (1 + newt, dest))
        return -1

            