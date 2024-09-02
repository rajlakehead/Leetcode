class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1 for i in range(len(nums))]

        for i in range(len(nums) - 1, - 1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)