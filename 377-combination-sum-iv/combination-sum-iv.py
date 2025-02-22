class Solution:
    def combinationSum4(self, nums: List[int], goal: int) -> int:
        
        memo = {}

        def dp(target):
            if target == 0:
                return 1
            if target in memo:
                return memo[target]

            count = 0

            for n in nums:
                if n <= target:
                    count += dp(target - n)
            memo[target] = count
            return memo[target]
        
        return dp(goal)