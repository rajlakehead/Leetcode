class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:


        n = len(nums)
        m = len(queries)
        unmarked_heap = [(val, i) for i,val in enumerate(nums)]
        heapq.heapify(unmarked_heap)
        marked = set()
        answer = []
        total = sum(nums)

        for index, k in queries:
            if index not in marked:
                marked.add(index)
                total -= nums[index]

            while k > 0 and unmarked_heap:
                val, idx = heapq.heappop(unmarked_heap)
                if idx not in marked:
                    total -= val
                    marked.add(idx)
                    k -= 1

            answer.append(total)

        return answer



        
        
            
            
        