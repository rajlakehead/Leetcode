class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        feq = defaultdict(int)
        left = 0
        res = 0
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while left < right and nums[right] * (right - left + 1) - currSum > k:
                currSum -= nums[left]
                left += 1
            res = max(res, (right - left + 1))
            
        return res



