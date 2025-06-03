class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        res = float('inf')

        for right in range(len(nums)):

            if (right - left + 1) >= k:
                res = min(res, nums[right] - nums[left])
                left += 1
        return res