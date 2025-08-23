class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        res = 0

        for right in range(1, len(nums)):

            if nums[right] > nums[left]:
                left += 1
                res += 1
        return res
