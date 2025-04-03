class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        resLen = float('inf')
        left = 0
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                resLen = min(resLen, right - left + 1)
                currSum -= nums[left]
                left += 1
        
        return resLen if resLen != float('inf') else 0



        