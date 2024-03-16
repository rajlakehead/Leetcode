class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        ones, zeros = 0, 0
        diff = {}

        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            else:
                ones += 1
            
            if ones - zeros not in diff:
                diff[ones - zeros] = i
            
            if zeros == ones:
                res = zeros + ones
            else:
                res = max(res, i - diff[ones - zeros])

        return res