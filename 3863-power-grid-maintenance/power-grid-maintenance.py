class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, x, y):
                xr, yr = self.find(x), self.find(y)
                if xr == yr:
                    return
                if self.rank[xr] < self.rank[yr]:
                    self.parent[xr] = yr
                elif self.rank[xr] > self.rank[yr]:
                    self.parent[yr] = xr
                else:
                    self.parent[yr] = xr
                    self.rank[xr] += 1

        # Step 1: Build DSU
        dsu = DSU(c + 1)
        for u, v in connections:
            dsu.union(u, v)

        # Step 2: Group stations by component
        comp_nodes = defaultdict(list)
        for node in range(1, c + 1):
            root = dsu.find(node)
            comp_nodes[root].append(node)

        # Step 3: Build a min-heap for each component
        comp_heap = {}
        for comp, nodes in comp_nodes.items():
            heap = nodes[:]
            heapq.heapify(heap)
            comp_heap[comp] = heap

        # Step 4: Online status
        online = [True] * (c + 1)

        # Step 5: Process queries
        results = []
        for t, x in queries:
            if t == 1:
                if online[x]:
                    results.append(x)
                else:
                    root = dsu.find(x)
                    heap = comp_heap[root]
                    # Lazy deletion of offline stations
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    if heap:
                        results.append(heap[0])
                    else:
                        results.append(-1)
            else:  # t == 2 → take station offline
                online[x] = False

        return results