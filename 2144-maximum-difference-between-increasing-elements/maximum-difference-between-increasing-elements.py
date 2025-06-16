class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curmax = nums[0]
        ans = -1

        for i in range(1, len(nums)):
            if nums[i] <= curmax:
                curmax = nums[i]
            else:
                ans = max(ans, nums[i] - curmax)
        return ans