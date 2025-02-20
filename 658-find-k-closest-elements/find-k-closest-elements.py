class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = []
        heapq.heapify(lst)

        for n in arr:
            heapq.heappush(lst, (-abs(n - x), -n))
            if len(lst) > k:
                heapq.heappop(lst)

        ans = []

        for _, num in lst:
            ans.append(-num)

        ans.sort()
        return ans
