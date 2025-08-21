class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        left = 0
        length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                length += 1
            else:
                res += ((length * (length + 1)) // 2)
                length = 0
        res += ((length * (length + 1)) // 2)
        return res