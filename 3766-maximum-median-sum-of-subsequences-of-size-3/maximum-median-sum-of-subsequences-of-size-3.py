class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 2
        ans = 0

        while i < j:
            ans += nums[j]
            i += 1
            j -= 2
        return ans
