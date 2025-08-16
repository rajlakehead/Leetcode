class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        minheap = [(0, 0, 0,True)]
        visited = set()
        n = len(moveTime)
        m = len(moveTime[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while minheap:
            t, r, c, odd = heapq.heappop(minheap)

            if r == n - 1 and c == m - 1:
                return t
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row, col) not in visited and row < n and col < m and row >= 0 and col >= 0:
                    if odd:
                        heapq.heappush(minheap, (1 + max(moveTime[row][col], t), row, col, not odd))
                    else:
                        heapq.heappush(minheap, (2 + max(moveTime[row][col], t), row, col, not odd))


        

