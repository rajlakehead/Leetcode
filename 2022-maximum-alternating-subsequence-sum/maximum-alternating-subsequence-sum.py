class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def dp(i, even):
            if i >= len(nums):
                return 0
            
            res = 0
            res = max(res, dp(i + 1, even))

            if even:
                res = max(res,nums[i] + dp(i + 1, not even))
            else:
                res = max(res, dp(i + 1, not even) - nums[i])
            
            return res
        return dp(0, True)

            