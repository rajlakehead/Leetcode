import heapq

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = 10**18
        dist = [[[INF, INF] for _ in range(n)] for _ in range(m)]
        
        # Start at (0,0) with odd step (we just entered it)
        dist[0][0][0] = (0+1)*(0+1)
        pq = [(dist[0][0][0], 0, 0, 0)]  # (cost, i, j, parity) parity=0: odd, 1: even
        
        while pq:
            cost, i, j, p = heapq.heappop(pq)
            if dist[i][j][p] < cost:
                continue
            
            if i == m-1 and j == n-1:
                return cost  # reached destination
            
            if p == 0:  # odd -> must move
                if i+1 < m:
                    new_cost = cost + (i+2)*(j+1)
                    if new_cost < dist[i+1][j][1]:
                        dist[i+1][j][1] = new_cost
                        heapq.heappush(pq, (new_cost, i+1, j, 1))
                if j+1 < n:
                    new_cost = cost + (i+1)*(j+2)
                    if new_cost < dist[i][j+1][1]:
                        dist[i][j+1][1] = new_cost
                        heapq.heappush(pq, (new_cost, i, j+1, 1))
            else:  # even -> must wait
                new_cost = cost + waitCost[i][j]
                if new_cost < dist[i][j][0]:
                    dist[i][j][0] = new_cost
                    heapq.heappush(pq, (new_cost, i, j, 0))
        
        return -1  # unreachable
