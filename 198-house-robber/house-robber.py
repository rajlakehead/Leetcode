class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(index):
            if index in memo:
                return memo[index]

            if index >= len(nums):
                return 0
            
            memo[index] = max(nums[index] + dp(index + 2), dp(index + 1))

            return memo[index]
            
        return dp(0)
