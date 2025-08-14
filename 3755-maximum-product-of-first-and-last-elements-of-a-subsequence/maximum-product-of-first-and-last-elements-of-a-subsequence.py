class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        mx, mn = nums[0], nums[0]
        res = float('-inf')

        for i in range(m - 1, len(nums)):
            mx = max(mx, nums[i - m + 1])
            mn = min(mn, nums[i - m + 1])
            res = max(res, mx * nums[i], mn * nums[i])
        return res