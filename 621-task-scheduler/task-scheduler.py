class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = (Counter(tasks))
        minheap = []
        for char, val in count.items():
            minheap.append([-val, char])
        
        q = collections.deque()
        heapq.heapify(minheap)
        currtime = 0

        while minheap or q:
            currtime += 1

            while q and q[0][0] <= currtime:
                _, ch, feq = q.popleft()
                heapq.heappush(minheap, [feq, ch])

            if minheap:
                freq, t = heapq.heappop(minheap)
                freq += 1

                if freq != 0:
                    q.append([currtime + n + 1, t , freq])
            
        return currtime


