class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = { i: [] for i in range(1, n + 1)}
        hashset = defaultdict(int)

        for u, v, t in times:
            adj[u].append((v, t))

        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        while minHeap:
            time, src = heapq.heappop(minHeap)

            hashset[src] = time

            if len(hashset) == n:
                return time

            for s, t in adj[src]:
                if s in hashset:
                    continue
                heapq.heappush(minHeap, (t + time, s))
        
        if len(hashset) != n:
            return -1
        return max(list(hashset.values()))
        