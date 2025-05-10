class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(1, target + 1):
            dp[i] = 0

            for n in nums:
                dp[i] += dp[i - n]
        
        return dp[target]