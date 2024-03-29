class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = max(nums)
        cnt = 0
        left, res = 0, 0

        for right in range(len(nums)):
            if nums[right] == n:
                cnt += 1
            
            while cnt >= k:
                if nums[left] == n:
                    cnt -= 1
                left += 1
            
            res += left
        return res