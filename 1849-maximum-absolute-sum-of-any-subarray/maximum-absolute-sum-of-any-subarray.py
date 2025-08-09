class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0
        res = 0

        for n in nums:
            curr += n
            res = max(res, curr)
            if curr < 0:
                curr = 0
        curr = 0
        for n in nums:
            curr += n
            res = max(res, abs(curr))
            if curr > 0:
                curr = 0
        return res