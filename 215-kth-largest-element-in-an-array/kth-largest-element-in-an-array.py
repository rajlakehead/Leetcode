import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for n in nums:
            heapq.heappush(minHeap, n)

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]