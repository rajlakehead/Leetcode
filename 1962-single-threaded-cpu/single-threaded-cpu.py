class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        index = 0
        for i in tasks:
            i.append(index)
            index += 1

        tasks.sort()
        heap.append((tasks[0][1], tasks[0][2]))
        currtime = tasks[0][0]
        res = []


        idx = 1

        while idx < len(tasks) or heap:

            while idx < len(tasks) and tasks[idx][0] <= currtime:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1

            if not heap:
                currtime = tasks[idx][0]
            else:
                t, i = heapq.heappop(heap)
                res.append(i)
                currtime += t

            
        return res



            
