class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []

        for char, val in count.items():
            maxHeap.append([-val, char])
        
        heapq.heapify(maxHeap)
        q = collections.deque()
        currtime = 0

        while maxHeap or q:
            currtime += 1

            while q and q[0][2] <= currtime:
                f, t, _ = q.popleft()
                heapq.heappush(maxHeap, [f, t])


            if maxHeap:
                feq, task = heapq.heappop(maxHeap)
                feq = -1 * feq
                feq -= 1

                if feq != 0:
                    q.append((-feq, task, currtime + n + 1))
        return currtime






