class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        minheap = [(0, k)]
        seen = set()
        ans = -1

        while minheap:

            t, node = heapq.heappop(minheap)

            if node in seen:
                continue

            seen.add(node)

            if len(seen) == n:
                ans = t
                break


            for nei, time in graph[node]:
                heapq.heappush(minheap, (t + time, nei))
        
        return ans