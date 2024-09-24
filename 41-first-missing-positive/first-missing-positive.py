class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        target = 1
        nums.sort()

        for n in nums:
            if n == target:
                target += 1
        return target