class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []
        res = []

        for n in arr:
            heapq.heappush(heap, (abs(n - x), n))

        while k:
            _, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        
        res.sort()
        
        return res


        