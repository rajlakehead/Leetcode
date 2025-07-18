class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        dp = [[1]*k for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                m = (nums[i] + nums[j]) % k
                dp[i][m] = max(dp[i][m], dp[j][m] + 1)
                ans = max(ans, dp[i][m])
        return ans