class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        vals = []
        for i, n in enumerate(nums):
            vals.append((i, n))
        
        vals.sort(key = lambda x : x[1], reverse = True)
        vals = sorted(vals[:k])

        res = [val for idx, val in vals]
        return res
