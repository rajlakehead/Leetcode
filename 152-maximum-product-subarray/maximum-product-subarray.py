class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            
            temp = currMax
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp * n, currMin * n, n)
            res = max(res, currMax)
        return res