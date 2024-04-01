class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        left = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            if (right - left + 1) == k:
                res = max(res, total / k)
                total -= nums[left]
                left += 1
        return res
