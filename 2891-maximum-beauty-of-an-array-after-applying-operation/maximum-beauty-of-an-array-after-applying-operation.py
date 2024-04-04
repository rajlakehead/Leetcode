class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        for r in range(len(nums)):
            if nums[r] - nums[l] > k * 2: l += 1
        return r - l + 1