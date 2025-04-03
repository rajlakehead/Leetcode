class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        currSum = 0

        for n in nums:
            currSum += n

            if currSum <= 0:
                currSum = 0
            else:
                res = max(res, currSum)
        return res