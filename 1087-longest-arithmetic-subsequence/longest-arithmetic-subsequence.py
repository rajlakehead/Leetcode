class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        ans = 0

        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = max(dp[i][diff], 1 + dp[j][diff])
                ans = max(ans, dp[i][diff])
        return ans + 1

