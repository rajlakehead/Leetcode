class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        q = []
        heapq.heappush(q, (0, (0, 0)))
        ans = 0
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            cost, d = heapq.heappop(q)
            r, c = d[0], d[1]

            if (r, c) in visited:
                continue

            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return cost


            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in visited:
                    continue
                newDiff = max(cost, (abs(heights[row][col] - heights[r][c])))
                heapq.heappush(q, (newDiff, (row, col)))

        return ans



            
            



