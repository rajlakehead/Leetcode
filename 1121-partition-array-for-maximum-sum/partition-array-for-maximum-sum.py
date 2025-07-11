class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @cache
        def dp(i):
            if i >= len(arr):
                return 0

            currMax = 0
            res = 0
            for j in range(i, min(i + k, len(arr))):
                currMax = max(currMax, arr[j])
                res = max(res, (currMax * (j - i + 1)) + dp(j + 1))
            return res
        return dp(0)

