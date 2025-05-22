from collections import defaultdict, deque
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the adjacency list
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        
        # Min-heap priority queue to store (cost, city, stops)
        pq = [(0, src, 0)]  # (cost, current city, number of stops)
        
        # Distance array to track the minimum cost to get to each city with a given stop count
        dist = {}
        
        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            # If we reach the destination within the required stops, return the cost
            if city == dst and stops <= k + 1:
                return cost
            
            # If we can still make more stops, explore the next flights
            if stops <= k:
                for neighbor, price in adj[city]:
                    new_cost = cost + price
                    if (neighbor, stops + 1) not in dist or dist[(neighbor, stops + 1)] > new_cost:
                        dist[(neighbor, stops + 1)] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        # If no valid route is found, return -1
        return -1
