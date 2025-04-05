class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        k = 1
        nums.sort()

        for n in nums:
            if n <= 0:
                continue
            elif n == k:
                k += 1
            else:
                return k
        return k
