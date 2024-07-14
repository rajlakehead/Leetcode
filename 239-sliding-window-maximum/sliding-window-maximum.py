class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = collections.deque()
        left, right = 0, 0

        while right < len(nums):

            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if right + 1 >= k:
                ans.append(nums[q[0]])
                left += 1
            right += 1
        
        return ans

        